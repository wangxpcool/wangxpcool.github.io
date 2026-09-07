"""Generate the static landing pages using only the Python standard library."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def page(title, body, active='home', prefix=''):
    credit = '<p class="refactor-credit" lang="en">Refactored by GPT-6 Astra</p>' if active == 'home' else ''
    def nav(label, href, key):
        current = ' aria-current="page"' if active == key else ''
        return f'<a href="{prefix}{href}"{current}>{label}</a>'
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="王学平的个人博客，记录技术实践、算法学习和生活思考。">
  <meta name="author" content="王学平">
  <title>{escape(title)} · wangxp</title>
  <link rel="stylesheet" href="{prefix}css/site.css">
  <script src="{prefix}js/site.js" defer></script>
</head>
<body>
  <a class="skip" href="#main">跳到正文</a>
  <div class="shell">
    <header class="header"><a class="brand" href="{prefix}index.html">wangxp<span>.</span></a>
      <nav class="nav" aria-label="主导航">{nav('文章', 'index.html', 'home')}{nav('关于', 'about.html', 'about')}<a class="github" href="https://github.com/wangxpcool">GitHub ↗</a></nav>
    </header>
    <main id="main">{body}</main>
    <footer class="footer"><div><span>© wangxp · 记录，让思考留下痕迹。</span>{credit}</div><a href="#main">回到顶部 ↑</a></footer>
  </div>
</body>
</html>
'''


def listing(posts, prefix=''):
    rows = []
    for post in posts:
        url = post['url']
        external = url.startswith('https://')
        if not external and not (ROOT / url).is_file():
            raise ValueError(f'Missing article: {url}')
        href = url if external else prefix + url
        date = f'<time datetime="{post["date"]}">{post["date"]}</time>' if post['date'] else '<span>微信文章</span>'
        rows.append(f'''<article class="post" data-category="{escape(post['category'])}">
          <div class="post-meta"><span class="tag">{escape(post['category'])}</span>{date}</div>
          <h3><a href="{escape(href, quote=True)}">{escape(post['title'])}<span class="arrow" aria-hidden="true">{'↗' if external else '→'}</span></a></h3>
          <p>{escape(post['summary'])}</p></article>''')
    return '\n'.join(rows)


def build():
    posts = json.loads((ROOT / 'data/posts.json').read_text(encoding='utf-8'))
    filters = ''.join(f'<button type="button" data-filter="{c}" aria-pressed="{str(c == "全部").lower()}">{c}</button>' for c in ['全部', '技术', '算法', '随笔'])
    body = f'''<section class="hero" aria-labelledby="intro-title">
      <div><p class="eyebrow">Notes on code & life / since 2016</p><h1 id="intro-title">在代码里探索，<br>在生活里<em>思考。</em></h1><p class="intro">你好，我是王学平。<br>这里记录技术实践、学习中的发现，以及生活里值得留下的片段。</p></div>
      <div class="hero-art" aria-hidden="true"><span>∴</span></div>
    </section>
    <div class="layout"><section aria-labelledby="articles-title">
      <div class="section-head"><h2 id="articles-title">文章与记录</h2><span class="count" id="result-count" role="status" aria-live="polite">{len(posts)} 篇文章</span></div>
      <div class="filters" role="group" aria-label="文章分类" hidden>{filters}</div>
      {listing(posts)}<p id="empty" class="empty" hidden>没有找到匹配的文章，试试其他关键词或分类。</p>
    </section><aside class="sidebar" aria-label="博客信息">
      <div class="search-box" hidden><label class="search-label" for="search">寻找一篇文章</label><input class="search" id="search" type="search" placeholder="搜索标题、关键词…" autocomplete="off"></div>
      <section class="side-block"><p class="eyebrow">A little about me</p><h2>王学平 / wangxp</h2><p>写代码，也写一些生活。<br>保持好奇，把学到的东西记下来。</p><a class="side-link" href="about.html">更多关于我 →</a></section>
      <section class="side-block"><h2>从这里开始</h2><p><a href="blogs/myFirstBlog.html">这个博客的第一篇文章 ↗</a></p><p><a href="Theme/myResume1.html">个人简历（历史版本） ↗</a></p></section>
      <p class="side-note">KEEP LEARNING.<br>KEEP WRITING.</p>
    </aside></div>'''
    (ROOT / 'index.html').write_text(page('文章与记录', body), encoding='utf-8')
    about = '''<section class="hero"><div><p class="eyebrow">Behind the words</p><h1>你好，<br>我是<em>王学平。</em></h1><p class="intro">wangxp / wangxpcool / sharping</p></div><div class="hero-art" aria-hidden="true"><span>W.</span></div></section>
    <div class="about-content"><p>这里是我的个人博客，记录编程、学习和生活中的思考。欢迎有着共同兴趣的朋友一起交流。</p><h2>关于这个小站</h2><p>2016 年，我写下了这里的第一篇文章。从 Java、Spring 到算法和日常随笔，博客保存了不同阶段的学习与想法。</p><p>你可以从<a href="index.html">文章列表</a>开始阅读，也可以看看<a href="blogs/myFirstBlog.html">这个网站的搭建故事</a>。</p><h2>找到我</h2><p>GitHub：<a href="https://github.com/wangxpcool">@wangxpcool ↗</a><br>QQ：963244208</p><h2>过去的介绍</h2><p>来自四川南充，曾到江苏淮安念书。旧版个人介绍记录了在上海工作的经历。</p><p><a href="Theme/myResume1.html">查看个人简历（历史版本） ↗</a></p></div>'''
    (ROOT / 'about.html').write_text(page('关于我', about, 'about'), encoding='utf-8')
    notes = [dict(title='为什么不去考验人性', url='notes/whyNotTestHumanity.html', date='2016-12-16', category='随笔', summary='关于人与人之间的信任和相处。')]
    (ROOT / 'notes/index.html').write_text(page('笔记', '<section class="hero"><div><p class="eyebrow">Personal notes</p><h1>一些<em>思考。</em></h1></div></section>' + listing(notes, '../'), 'notes', '../'), encoding='utf-8')
    print(f'Generated index.html, about.html, notes/index.html ({len(posts)} articles).')


if __name__ == '__main__':
    build()
