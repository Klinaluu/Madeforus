#!/usr/bin/env python3
"""Gộp index.html + các module JS thành một file HTML chạy được bằng double-click.

Trình duyệt chặn ES module khi mở qua file:// nên mỗi module được bọc trong IIFE và
import/export đổi thành biến thường. Ảnh vẫn nạp từ thư mục assets/ bên cạnh.

    python3 tools/build_standalone.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES = ["config", "assets", "levels", "audio", "engine", "main"]  # theo thứ tự phụ thuộc
ENTRY_TAG = '<script type="module" src="js/main.js"></script>'


def bundle_module(name, root):
    src = open(os.path.join(root, "js", f"{name}.js"), encoding="utf-8").read()
    exports = []

    def strip_export(m):
        exports.append(m.group(2))
        return m.group(1)

    src = re.sub(r"^export ((?:const|let|var|function|class) ([A-Za-z_$][\w$]*))", strip_export, src, flags=re.M)
    src = re.sub(
        r'^import \{([^}]*)\} from "\./(\w+)\.js";',
        lambda m: f'const {{{" ".join(m.group(1).split())}}} = __mod_{m.group(2)};',
        src,
        flags=re.M | re.S,
    )
    return f"const __mod_{name} = (() => {{\n{src}\nreturn {{ {', '.join(exports)} }};\n}})();\n"


def build(root=ROOT, out_name="Made for Us.html"):
    js = "\n".join(bundle_module(m, root) for m in MODULES)
    html = open(os.path.join(root, "index.html"), encoding="utf-8").read()
    if ENTRY_TAG not in html:
        raise SystemExit("Khong tim thay the script trong index.html")
    html = html.replace(ENTRY_TAG, "<script>\n" + js + "\n</script>")
    out = os.path.join(root, out_name)
    open(out, "w", encoding="utf-8").write(html)
    print(f"-> {out} ({len(html) // 1024} KB)")
    return out


if __name__ == "__main__":
    build()
