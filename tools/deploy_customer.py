#!/usr/bin/env python3
"""Đưa bản game của một khách lên GitHub Pages.

    # 1. Tạo sẵn một repo TRỐNG (public) trên github.com, vd: Klinaluu/linh-tung
    # 2. Chạy:
    python3 tools/deploy_customer.py linh-tung https://github.com/Klinaluu/linh-tung.git

Script tự: dựng lại bản build với đúng đường dẫn Pages (để ảnh preview khi gửi link
hiển thị đúng), khởi tạo git trong dist/<slug>, commit và push lên nhánh main.

Sau khi push, bật Pages một lần trong Settings → Pages → Deploy from a branch →
main / (root). Lần sau chỉ cần chạy lại script là link tự cập nhật.
"""
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIT_NAME = "Lina Luu"
GIT_EMAIL = "luukhanhlinh0710@gmail.com"


def run(cmd, cwd, check=True):
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)


def pages_url(repo_url):
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", repo_url)
    if not m:
        # repo cuc bo (dung khi thu nghiem): khong co trang Pages
        name = os.path.splitext(os.path.basename(repo_url.rstrip("/")))[0]
        return "", "", name
    owner, repo = m.group(1), m.group(2)
    return f"https://{owner.lower()}.github.io/{repo}/", owner, repo


def main():
    if len(sys.argv) < 3:
        sys.exit("Cach dung: python3 tools/deploy_customer.py <slug> <git-url> [--no-build]")
    slug = sys.argv[1].strip().lower()
    repo_url = sys.argv[2]
    url, owner, repo = pages_url(repo_url)

    if "--no-build" not in sys.argv:
        args = [sys.executable, os.path.join(ROOT, "tools", "build_customer.py"), slug]
        if url:
            args += ["--url", url]
        r = subprocess.run(args, cwd=ROOT)
        if r.returncode:
            sys.exit("Build that bai.")

    dist = os.path.join(ROOT, "dist", slug)
    if not os.path.isdir(dist):
        sys.exit(f"Chua co {dist} — chay tools/build_customer.py {slug} truoc.")

    if not os.path.isdir(os.path.join(dist, ".git")):
        run(["git", "init", "-q", "-b", "main"], dist)
        run(["git", "remote", "add", "origin", repo_url], dist)
    else:
        run(["git", "remote", "set-url", "origin", repo_url], dist)

    # repo da co noi dung thi noi tiep lich su, chua co thi commit dau tien
    fetched = run(["git", "fetch", "-q", "origin", "main"], dist, check=False).returncode == 0
    if fetched:
        run(["git", "reset", "-q", "--mixed", "FETCH_HEAD"], dist)
    run(["git", "add", "-A"], dist)
    status = run(["git", "status", "--porcelain"], dist).stdout.strip()
    if status:
        run(["git", "-c", f"user.name={GIT_NAME}", "-c", f"user.email={GIT_EMAIL}",
             "commit", "-q", "-m", f"Ban game cho {slug}"], dist)
    run(["git", "push", "-q", "-u", "origin", "main"], dist)

    print(f"\nDa push len {repo_url}")
    if not url:
        print("(Repo cuc bo — khong co link GitHub Pages)")
        return
    print(f"Link game: {url}")
    try:
        code = urllib.request.urlopen(url, timeout=10).getcode()
        print(f"Trang da song (HTTP {code}).")
    except Exception:
        print("Chua thay trang — neu day la lan dau, bat Pages tai:")
        print(f"  https://github.com/{owner}/{repo}/settings/pages")
        print("  Source: Deploy from a branch · Branch: main · Thu muc: / (root) · Save")
        print("Doi ~1 phut roi mo lai link.")
    print(f"\nGui khach: link o tren + file dist/{slug}.zip (ban choi offline)")
    print("Nho kem huong dan: iPhone/iPad mo bang Safari → Chia se → Them vao MH chinh")


if __name__ == "__main__":
    main()
