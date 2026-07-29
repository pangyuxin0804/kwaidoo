# -*- coding: utf-8 -*-
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'C:\Users\20170\Desktop\学习报告'

# 旧的前缀 → 新的相对于工作区根的路径
RULES = {
    '../assets/HTTP接口操作指南_庞宇新_assets/':     'assets/HTTP接口操作指南_庞宇新_assets/',
    '../assets/HTTP接口操作指南_欧阳荣康_assets/':    'assets/HTTP接口操作指南_欧阳荣康_assets/',
    '../assets/PAAS环境申请操作指南_庞宇新_assets/':  'assets/PAAS环境申请操作指南_庞宇新_assets/',
    '../assets/PAAS环境申请操作指南_欧阳荣康_assets/': 'assets/PAAS环境申请操作指南_欧阳荣康_assets/',
    '../assets/定时任务创建操作指南_庞宇新_assets/':  'assets/定时任务创建操作指南_庞宇新_assets/',
    '../assets/定时任务创建操作指南_欧阳荣康_assets/': 'assets/定时任务创建操作指南_欧阳荣康_assets/',
    '../assets/环境引用数据库更改_庞宇新_assets/':    'assets/环境引用数据库更改_庞宇新_assets/',
    '../assets/环境引用数据库更改_欧阳荣康_assets/':  'assets/环境引用数据库更改_欧阳荣康_assets/',
    '../assets/平台环境更新学习报告_庞宇新_assets/':  'assets/平台环境更新学习报告_庞宇新_assets/',
    '../assets/平台环境更新学习报告_欧阳荣康_assets/': 'assets/平台环境更新学习报告_欧阳荣康_assets/',
}

count = 0
for root, dirs, files in os.walk(BASE):
    for fname in files:
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        original = content
        for old_prefix, new_prefix in RULES.items():
            content = content.replace(old_prefix, new_prefix)
        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            rel = os.path.relpath(fpath, BASE)
            print(f'[OK] {rel}')
            count += 1

print(f'\n共修改了 {count} 个文件')
