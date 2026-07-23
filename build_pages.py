"""Ponytail: one script generates all 4 pages. Pure CSS, no Tailwind CDN."""
import pathlib

DIR = pathlib.Path(__file__).parent

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Geist',sans-serif;background:#0b1326;color:#dae2fd;-webkit-font-smoothing:antialiased}
::selection{background:rgba(195,192,255,.3)}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#2d3449;border-radius:8px}
a{text-decoration:none}
button{cursor:pointer;font-family:inherit}
input,textarea,select{font-family:inherit}
"""

COMMON = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=block" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
body{font-family:'Inter',sans-serif;background:#0b1326;color:#dae2fd;-webkit-font-smoothing:antialiased}
*{margin:0;padding:0;box-sizing:border-box}
::selection{background:rgba(195,192,255,.3)}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#2d3449;border-radius:8px}
a{text-decoration:none}
button{cursor:pointer;font-family:inherit}
input,textarea,select{font-family:inherit}
"""

# ─── LANDING PAGE ───
LANDING = COMMON + """
<style>
.nav{display:flex;justify-content:space-between;align-items:center;height:40px;padding:0 16px;width:100%;position:fixed;top:0;z-index:50;background:#0b1326;border-bottom:1px solid #464555}
.nav-l{display:flex;align-items:center;gap:24px}
.nav-brand{font-size:24px;font-weight:700;color:#dae2fd;letter-spacing:-.01em}
.nav-links{display:none;align-items:center;gap:8px}
@media(min-width:768px){.nav-links{display:flex}}
.nav-links a{font-size:11px;font-weight:600;color:#c7c4d8;padding:4px 8px;border-radius:4px;letter-spacing:.05em;text-transform:uppercase;font-family:'JetBrains Mono',monospace;transition:all .2s}
.nav-links a:hover{background:rgba(45,52,73,.5)}
.nav-links a.active{color:#c3c0ff;border-bottom:2px solid #c3c0ff}
.nav-r{display:flex;align-items:center;gap:8px}
.nav-search{display:none;align-items:center;gap:4px;padding:4px 12px;border:1px solid #464555;border-radius:8px;font-size:14px;color:#c7c4d8;background:#131b2e}
@media(min-width:640px){.nav-search{display:flex}}
.nav-search .m{font-size:16px}
.nav-icon{background:none;border:none;color:#c7c4d8;padding:4px;border-radius:4px;transition:all .2s;line-height:1}
.nav-icon:hover{background:rgba(45,52,73,.5)}
.nav-icon .m{font-size:20px}
.nav-div{width:1px;height:24px;background:#464555;margin:0 4px}
.nav-btn{padding:4px 16px;background:#4f46e5;color:#fff;border:none;border-radius:4px;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:all .2s}
.nav-btn:hover{filter:brightness(1.1)}
.nav-avatar{width:32px;height:32px;border-radius:50%;border:1px solid #464555;overflow:hidden;cursor:pointer;transition:all .2s;margin-left:8px}
.nav-avatar:hover{border-color:#c3c0ff}
.nav-avatar img{width:100%;height:100%;object-fit:cover}

.hero{position:relative;padding:128px 16px 80px;overflow:hidden;min-height:819px;display:flex;flex-direction:column;justify-content:center;align-items:center}
.hero-badge{display:inline-flex;align-items:center;gap:4px;padding:4px 8px;border-radius:999px;border:1px solid rgba(195,192,255,.3);background:rgba(195,192,255,.05);color:#c3c0ff;margin-bottom:24px}
.hero-badge-dot{width:8px;height:8px;border-radius:50%;background:#c3c0ff;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.hero-badge span{font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.hero h1{font-size:48px;line-height:56px;letter-spacing:-.02em;font-weight:700;text-align:center;color:#dae2fd;max-width:4xl}
@media(min-width:768px){.hero h1{font-size:64px;line-height:72px}}
.hero h1 em{color:#c3c0ff;font-style:italic}
.hero p{font-size:16px;color:#c7c4d8;text-align:center;max-width:640px;margin:16px auto 0;line-height:1.6}
.hero-btns{display:flex;flex-direction:column;gap:16px;margin-top:48px;width:100%;max-width:320px}
@media(min-width:640px){.hero-btns{flex-direction:row;width:auto}}
.hero-btn-primary{padding:16px 24px;background:#4f46e5;color:#fff;border:none;border-radius:8px;font-size:16px;font-weight:600;transition:all .2s;box-shadow:0 4px 20px rgba(79,70,229,.3)}
.hero-btn-primary:hover{filter:brightness(1.1)}
.hero-btn-secondary{padding:16px 24px;background:transparent;border:1px solid #464555;color:#dae2fd;border-radius:8px;font-size:16px;font-weight:600;transition:all .2s}
.hero-btn-secondary:hover{background:rgba(45,52,73,.5)}

.showcase{padding:0 16px 128px;max-width:1152px;margin:0 auto}
.showcase-wrap{position:relative}
.showcase-glow{position:absolute;inset:-4px;background:linear-gradient(90deg,rgba(195,192,255,.5),rgba(137,206,255,.5));border-radius:12px;filter:blur(16px);opacity:.2;transition:opacity .3s}
.showcase-wrap:hover .showcase-glow{opacity:.3}
.showcase-panel{position:relative;background:rgba(23,31,51,.7);backdrop-filter:blur(12px);border:1px solid #464555;border-radius:12px;overflow:hidden;box-shadow:0 25px 50px rgba(0,0,0,.5)}
.showcase-toolbar{height:32px;background:#222a3d;border-bottom:1px solid #464555;display:flex;align-items:center;padding:0 16px;justify-content:space-between}
.showcase-dots{display:flex;gap:6px}
.showcase-dot{width:12px;height:12px;border-radius:50%}
.showcase-dot.r{background:rgba(255,180,171,.4)}
.showcase-dot.y{background:rgba(137,206,255,.4)}
.showcase-dot.p{background:rgba(195,192,255,.4)}
.showcase-title{font-size:11px;font-weight:600;color:#c7c4d8;opacity:.6;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.showcase-body{display:flex;height:600px}
.showcase-sidebar{width:260px;background:#131b2e;border-right:1px solid #464555;display:none;flex-direction:column;padding:16px 0}
@media(min-width:768px){.showcase-sidebar{display:flex}}
.showcase-sidebar-head{padding:0 16px 16px;display:flex;justify-content:space-between;align-items:center}
.showcase-sidebar-head span{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.15em;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.showcase-sidebar-head .m{font-size:14px}
.showcase-sidebar-item{display:flex;align-items:center;gap:8px;padding:6px 16px;font-size:14px;color:#c7c4d8;transition:all .2s;border-left:2px solid transparent}
.showcase-sidebar-item:hover{background:rgba(45,52,73,.3)}
.showcase-sidebar-item.active{border-left-color:#c3c0ff;background:rgba(195,192,255,.1);color:#c3c0ff}
.showcase-sidebar-item.sub{padding-left:32px}
.showcase-sidebar-item .m{font-size:18px}
.showcase-editor{flex:1;background:#060e20;position:relative;overflow:hidden}
.showcase-code{padding:24px;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:22px;position:relative}
.showcase-code-bg{position:absolute;inset:0;pointer-events:none;opacity:.03;background-image:radial-gradient(#4f46e5 .5px,transparent .5px);background-size:20px 20px}
.code-line{display:flex;gap:16px}
.code-line.faded{opacity:.5}
.code-line .ln{width:32px;color:rgba(70,69,85,.4);user-select:none;text-align:right}
.kw{color:#c3c0ff;font-weight:600}
.st{color:#89ceff}
.cm{color:#918fa1;font-style:italic}
.fn{color:#ffb695}
.cursor-anim{position:absolute;left:180px;top:0;height:20px;width:2px;background:#c3c0ff;animation:blink 1s step-end infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.cursor-label{position:absolute;left:180px;top:-20px;background:#c3c0ff;padding:2px 6px;border-radius:2px;font-size:9px;font-weight:700;color:#0f0069;font-family:'JetBrains Mono',monospace}
.ai-box{margin:16px 0 16px 48px;padding:16px;background:rgba(23,31,51,.7);border:1px solid rgba(195,192,255,.4);border-left:4px solid #4f46e5;border-radius:0 8px 8px 0}
.ai-box-head{display:flex;align-items:center;gap:4px;margin-bottom:8px}
.ai-box-head .m{font-size:16px;color:#c3c0ff}
.ai-box-head span{font-size:11px;font-weight:600;color:#c3c0ff;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.ai-box p{font-size:14px;color:#c7c4d8;font-style:italic;margin-bottom:12px}
.ai-box-btns{display:flex;gap:8px}
.ai-box-btns button{padding:4px 12px;border-radius:4px;font-size:12px;font-weight:600;border:none}
.ai-box-btns .accept{background:#c3c0ff;color:#0f0069}
.ai-box-btns .ignore{background:transparent;border:1px solid #464555;color:#c7c4d8}

.social-proof{padding:64px 16px;border-y:1px solid #464555;background:#131b2e}
.social-proof p{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.15em;text-align:center;text-transform:uppercase;opacity:.6;margin-bottom:24px;font-family:'JetBrains Mono',monospace}
.social-proof-logos{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:48px;opacity:.5;filter:grayscale(1);transition:all .5s}
.social-proof-logos:hover{filter:grayscale(0)}
.social-proof-logos .logo{display:flex;align-items:center;gap:8px}
.social-proof-logos .m{font-size:32px}
.social-proof-logos span{font-size:24px;font-weight:700}

.features{padding:128px 16px;max-width:1152px;margin:0 auto;display:grid;grid-template-columns:1fr;gap:24px}
@media(min-width:768px){.features{grid-template-columns:repeat(3,1fr)}}
.feature-card{padding:24px;border:1px solid #464555;background:#060e20;border-radius:12px;transition:all .3s}
.feature-card:hover{border-color:rgba(195,192,255,.5)}
.feature-icon{width:48px;height:48px;background:rgba(195,192,255,.1);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#c3c0ff;margin-bottom:16px;transition:transform .3s}
.feature-card:hover .feature-icon{transform:scale(1.1)}
.feature-icon .m{font-size:28px}
.feature-card h3{font-size:24px;line-height:32px;letter-spacing:-.01em;font-weight:600;margin-bottom:8px}
.feature-card p{font-size:14px;line-height:20px;color:#c7c4d8}

.bento{padding:0 16px 128px;max-width:1152px;margin:0 auto;display:grid;grid-template-columns:1fr;gap:24px}
@media(min-width:768px){.bento{grid-template-columns:repeat(2,1fr)}}
.bento-wide{grid-column:1/-1;position:relative;background:rgba(23,31,51,.7);backdrop-filter:blur(12px);border-radius:16px;padding:48px;display:flex;flex-direction:column;gap:24px;min-height:400px;border:1px solid #464555;overflow:hidden}
@media(min-width:768px){.bento-wide{flex-direction:row;align-items:center}}
.bento-wide-l{flex:1}
.bento-wide-l .label{font-size:11px;font-weight:600;color:#c3c0ff;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;margin-bottom:8px}
.bento-wide-l h2{font-size:32px;line-height:40px;font-weight:700;margin-bottom:12px}
.bento-wide-l p{font-size:16px;color:#c7c4d8;line-height:1.6;margin-bottom:16px}
.bento-wide-l ul{list-style:none;display:flex;flex-direction:column;gap:8px}
.bento-wide-l li{display:flex;align-items:center;gap:8px;color:#c7c4d8;font-size:14px}
.bento-wide-l li .m{color:#c3c0ff;font-size:20px}
.bento-wide-r{flex:1;width:100%;min-height:250px;border-radius:12px;border:1px solid #464555;background:rgba(0,0,0,.4);overflow:hidden;position:relative}
.bento-wide-r pre{position:absolute;inset:0;padding:16px;font-family:'JetBrains Mono',monospace;font-size:12px;color:#c3c0ff;opacity:.3;line-height:1.6}
.bento-wide-r .icon-center{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.bento-wide-r .icon-center .m{font-size:64px;color:#c3c0ff;opacity:.5;animation:pulse 2s infinite}
.bento-card{background:rgba(23,31,51,.7);backdrop-filter:blur(12px);border-radius:16px;padding:24px;border:1px solid #464555;transition:all .3s}
.bento-card:hover{background:rgba(34,42,61,.7)}
.bento-card-head{display:flex;align-items:center;gap:16px;margin-bottom:12px}
.bento-card-icon{width:40px;height:40px;border-radius:4px;display:flex;align-items:center;justify-content:center}
.bento-card-icon .m{font-size:20px}
.bento-card-icon.green{background:rgba(74,222,128,.1);color:#4ade80}
.bento-card-icon.blue{background:rgba(137,206,255,.1);color:#89ceff}
.bento-card h3{font-size:24px;line-height:32px;font-weight:600}
.bento-card p{font-size:14px;color:#c7c4d8;line-height:1.6}

.cta{padding:128px 16px;text-align:center;border-top:1px solid #464555;position:relative;overflow:hidden}
.cta h2{font-size:48px;line-height:56px;letter-spacing:-.02em;font-weight:700;margin-bottom:16px}
.cta p{font-size:16px;color:#c7c4d8;max-width:576px;margin:0 auto 32px;line-height:1.6}
.cta button{padding:24px 48px;background:#c3c0ff;color:#1d00a5;border:none;border-radius:12px;font-size:24px;line-height:32px;font-weight:600;transition:all .2s;box-shadow:0 25px 50px rgba(195,192,255,.3)}
.cta button:hover{filter:brightness(1.1)}
.cta button:active{transform:scale(.95)}
.cta .sub{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.15em;text-transform:uppercase;opacity:.6;margin-top:16px;font-family:'JetBrains Mono',monospace}

.footer{background:#060e20;border-top:1px solid #464555;width:100%}
.footer-inner{display:flex;flex-direction:column;align-items:center;gap:16px;padding:24px;max-width:1280px;margin:0 auto}
@media(min-width:768px){.footer-inner{flex-direction:row;justify-content:space-between}}
.footer-brand{text-align:center}
@media(min-width:768px){.footer-brand{text-align:left}}
.footer-brand .name{font-size:24px;font-weight:700;color:#dae2fd;letter-spacing:-.01em}
.footer-brand .copy{font-size:14px;color:#c7c4d8;margin-top:4px}
.footer-links{display:flex;gap:16px;flex-wrap:wrap;justify-content:center}
.footer-links a{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:color .2s}
.footer-links a:hover{color:#c3c0ff}
.footer-social{display:flex;gap:8px}
.footer-social button{width:32px;height:32px;border:1px solid #464555;border-radius:4px;background:transparent;display:flex;align-items:center;justify-content:center;color:#c7c4d8;transition:all .2s}
.footer-social button:hover{background:rgba(45,52,73,.5)}
.footer-social .m{font-size:20px}
</style>
</head>
<body>
<nav class="nav">
<div class="nav-l">
<a href="/" style="text-decoration:none;color:#dae2fd"><span class="nav-brand">BuildTogether</span></a>
<div class="nav-links">
<a href="/">IDE</a>
<a href="/dashboard">Projects</a>
<a href="/team">Team</a>
<a class="active" href="/landing">Landing</a>
</div>
</div>
<div class="nav-r">
<div class="nav-search"><span class="m material-symbols-outlined">search</span><span>Search codebase...</span></div>
<button class="nav-icon"><span class="m material-symbols-outlined">notifications</span></button>
<button class="nav-icon"><span class="m material-symbols-outlined">history</span></button>
<div class="nav-div"></div>
<button class="nav-btn">Run</button>
<div class="nav-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDFZaWxNq_LcQ1z2hmI8tFfXlYHkqj3eOzZErpg-a3n5Tija1Y9lRyGyJoLwqWXZWlyHcaOPit3YF6nPjMO_9xbPEcVQD70vMQjc5Z6EwQBgrYzXRbb_BR8czv6royCh9PdAksiKfCpjmGnwDpW9_PgzvLspwGASplUS_GAxH-aAY0RNB0aStEeNH-c5nATIrirLwDeqd03Cv8ZJgjKAhF7sxuvczgc2ydBr8X5y8D2WoKtyAZjN5vT4Q" alt=""></div>
</div>
</nav>

<header class="hero">
<div style="max-width:896px;text-align:center;z-index:10">
<div class="hero-badge"><div class="hero-badge-dot"></div><span>v2.0 Beta: Multi-model AI Integration is Live</span></div>
<h1>Code at the <em>speed of thought</em>, together.</h1>
<p>The AI-native collaborative IDE that eliminates friction. Real-time synchronization for global teams, context-aware pair programming, and instant cloud-native environments.</p>
<div class="hero-btns">
<button class="hero-btn-primary">Get Started for Free</button>
<button class="hero-btn-secondary">Request a Demo</button>
</div>
</div>
</header>

<section class="showcase">
<div class="showcase-wrap">
<div class="showcase-glow"></div>
<div class="showcase-panel">
<div class="showcase-toolbar">
<div class="showcase-dots"><div class="showcase-dot r"></div><div class="showcase-dot y"></div><div class="showcase-dot p"></div></div>
<div class="showcase-title">src/main.ts — BuildTogether</div>
<div style="width:48px"></div>
</div>
<div class="showcase-body">
<div class="showcase-sidebar">
<div class="showcase-sidebar-head"><span>Workspace</span><span class="m material-symbols-outlined">add</span></div>
<div class="showcase-sidebar-item active"><span class="m material-symbols-outlined">folder_open</span><span>src</span></div>
<div class="showcase-sidebar-item sub"><span class="m material-symbols-outlined">javascript</span><span>app.ts</span></div>
<div class="showcase-sidebar-item sub"><span class="m material-symbols-outlined">settings</span><span>config.json</span></div>
</div>
<div class="showcase-editor">
<div class="showcase-code">
<div class="showcase-code-bg"></div>
<div class="code-line faded"><span class="ln">1</span><span><span class="kw">import</span> { Engine } <span class="kw">from</span> <span class="st">"@core/engine"</span>;</span></div>
<div class="code-line faded"><span class="ln">2</span><span></span></div>
<div class="code-line"><span class="ln">3</span><span><span class="kw">async function</span> <span class="fn">initializeWorkspace</span>() {</span></div>
<div class="code-line"><span class="ln">4</span><span>  <span class="kw">const</span> engine = <span class="kw">new</span> <span class="fn">Engine</span>({</span></div>
<div class="code-line"><span class="ln">5</span><span>    cluster: <span class="st">"us-west-2"</span>,</span></div>
<div class="code-line" style="position:relative"><span class="ln">6</span><span>    realtime: <span class="kw">true</span></span><div class="cursor-anim"></div><div class="cursor-label">Alex (Writing...)</div></div>
<div class="code-line"><span class="ln">7</span><span>  });</span></div>
<div class="code-line"><span class="ln">8</span><span></span></div>
<div class="ai-box">
<div class="ai-box-head"><span class="m material-symbols-outlined" style="font-variation-settings:'FILL' 1">auto_awesome</span><span>AI PAIR ASSISTANT</span></div>
<p>Would you like to implement the error handler for the engine initialization?</p>
<div class="ai-box-btns"><button class="accept">Accept (Tab)</button><button class="ignore">Ignore (Esc)</button></div>
</div>
</div>
</div>
</div>
</div>
</div>
</section>

<section class="social-proof">
<p>Trusted by modern engineering teams</p>
<div class="social-proof-logos">
<div class="logo"><span class="m material-symbols-outlined">cloud_done</span><span>BetterBytes</span></div>
<div class="logo"><span class="m material-symbols-outlined">hub</span><span>CloudFlow</span></div>
<div class="logo"><span class="m material-symbols-outlined">terminal</span><span>DevKernel</span></div>
<div class="logo"><span class="m material-symbols-outlined">bolt</span><span>VeloSync</span></div>
</div>
</section>

<section class="features">
<div class="feature-card"><div class="feature-icon"><span class="m material-symbols-outlined">sync</span></div><h3>Real-time Synchronization</h3><p>Industry-leading CRDT implementation ensures sub-50ms sync latency. Collaborate with thousands of developers on the same file without conflicts.</p></div>
<div class="feature-card"><div class="feature-icon"><span class="m material-symbols-outlined">auto_awesome</span></div><h3>AI-Powered Pair Programming</h3><p>Context-aware AI that understands your entire codebase, not just the active file. Get high-precision suggestions that actually compile.</p></div>
<div class="feature-card"><div class="feature-icon"><span class="m material-symbols-outlined">contacts</span></div><h3>Instant Provisioning</h3><p>Zero-config environments spin up in under 2 seconds. Fully containerized workspaces that match your production environment perfectly.</p></div>
</section>

<section class="bento">
<div class="bento-wide">
<div class="bento-wide-l">
<div class="label">SCALABILITY</div>
<h2>Infinite Scale Workspace for Massive Repos</h2>
<p>BuildTogether handles mono-repos with millions of files without slowing down. Our proprietary indexing engine keeps search and navigation instantaneous.</p>
<ul>
<li><span class="m material-symbols-outlined">check_circle</span><span>Sparse checkout architecture</span></li>
<li><span class="m material-symbols-outlined">check_circle</span><span>Cloud-native symbol indexing</span></li>
</ul>
</div>
<div class="bento-wide-r">
<pre>// Indexing shard 892...<br>// Loaded 1.2M symbols in 0.4s<br>// Cache hit: 99.8%<br>// Node status: Healthy<br>// Indexing shard 893...<br>// Loaded 1.2M symbols in 0.4s<br>// Cache hit: 99.8%<br>// Node status: Healthy</pre>
<div class="icon-center"><span class="m material-symbols-outlined">database</span></div>
</div>
</div>
<div class="bento-card">
<div class="bento-card-head"><div class="bento-card-icon green"><span class="m material-symbols-outlined">verified_user</span></div><h3>Secure by Design</h3></div>
<p>Enterprise-grade security is baked into the core. SOC2 Type II compliant, end-to-end encryption for code in transit and at rest, and per-workspace network isolation.</p>
</div>
<div class="bento-card">
<div class="bento-card-head"><div class="bento-card-icon blue"><span class="m material-symbols-outlined">api</span></div><h3>API First</h3></div>
<p>Extensible by design. Build custom workflows with our robust SDK and CLI tools. Integrate directly with your CI/CD pipelines and internal developer portals.</p>
</div>
</section>

<section class="cta">
<h2>Ready to build the future?</h2>
<p>Join over 50,000 developers building better software together. Start for free, no credit card required.</p>
<div><button>Sign Up for BuildTogether</button></div>
<div class="sub">Available on Windows, macOS, and Linux</div>
</section>

<footer class="footer">
<div class="footer-inner">
<div class="footer-brand"><div class="name">BuildTogether</div><div class="copy">© 2024 BuildTogether. Technical Precision.</div></div>
<div class="footer-links">
<a href="#">Privacy</a><a href="#">Terms</a><a href="#">Documentation</a><a href="#">API</a><a href="#">Status</a>
</div>
<div class="footer-social">
<button><span class="m material-symbols-outlined">terminal</span></button>
<button><span class="m material-symbols-outlined">public</span></button>
</div>
</div>
</footer>
</body></html>"""

# ─── TEAM PAGE ───
TEAM = COMMON + """
<style>
.layout{display:flex;flex-direction:column;height:100vh;overflow:hidden}
.nav{display:flex;justify-content:space-between;align-items:center;height:40px;padding:0 16px;width:100%;z-index:50;background:#0b1326;border-bottom:1px solid #464555;flex-shrink:0}
.nav-l{display:flex;align-items:center;gap:24px}
.nav-brand{font-size:24px;font-weight:700;color:#dae2fd;letter-spacing:-.01em}
.nav-links{display:none;align-items:center;gap:8px}
@media(min-width:768px){.nav-links{display:flex}}
.nav-links a{font-size:13px;color:#c7c4d8;padding:4px 8px;border-radius:4px;transition:all .2s;font-family:'Inter',sans-serif}
.nav-links a:hover{background:rgba(45,52,73,.5)}
.nav-links a.active{color:#c3c0ff;border-bottom:2px solid #c3c0ff;font-weight:600}
.nav-r{display:flex;align-items:center;gap:8px}
.nav-search{position:relative}
.nav-search input{background:#131b2e;border:1px solid #464555;border-radius:8px;padding:4px 32px 4px 12px;font-size:14px;color:#dae2fd;outline:none;width:256px;transition:all .2s}
.nav-search input:focus{border-color:#c3c0ff}
.nav-search .m{position:absolute;right:8px;top:50%;transform:translateY(-50%);font-size:16px;color:#c7c4d8}
.nav-icon{background:none;border:none;color:#c7c4d8;padding:4px;border-radius:4px;transition:all .2s;line-height:1}
.nav-icon:hover{background:rgba(45,52,73,.5)}
.nav-icon .m{font-size:20px}
.nav-avatar{width:32px;height:32px;border-radius:50%;border:1px solid #464555;overflow:hidden;margin-left:8px}
.nav-avatar img{width:100%;height:100%;object-fit:cover}

.body{display:flex;flex:1;overflow:hidden}
.sidebar{width:260px;background:#131b2e;border-right:1px solid #464555;display:none;flex-direction:column;justify-content:space-between;padding:16px 0;flex-shrink:0}
@media(min-width:768px){.sidebar{display:flex}}
.sidebar-top{display:flex;flex-direction:column;gap:8px}
.sidebar-head{padding:0 16px 16px}
.sidebar-head-label{display:flex;align-items:center;gap:8px;margin-bottom:4px}
.sidebar-head-label .icon{width:24px;height:24px;background:#00a2e6;border-radius:4px;display:flex;align-items:center;justify-content:center}
.sidebar-head-label .icon .m{font-size:14px;color:#00344e}
.sidebar-head-label span{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.15em;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.sidebar-head-sub{font-size:14px;color:#dae2fd;opacity:.6}
.sidebar-nav{display:flex;flex-direction:column}
.sidebar-nav-item{display:flex;align-items:center;gap:12px;padding:8px 16px;color:#c7c4d8;border-left:2px solid transparent;transition:all .2s;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.sidebar-nav-item:hover{background:rgba(45,52,73,.3)}
.sidebar-nav-item.active{border-left-color:#c3c0ff;background:rgba(195,192,255,.1);color:#c3c0ff}
.sidebar-nav-item .m{font-size:20px}
.sidebar-bottom{display:flex;flex-direction:column}
.sidebar-bottom .sidebar-nav-item{border-left:none}

.main{flex:1;overflow-y:auto;background:#0b1326;padding:24px;position:relative}
.main-inner{max-width:1152px;margin:0 auto}
.page-header{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:48px}
.page-header h1{font-size:48px;line-height:56px;letter-spacing:-.02em;font-weight:700;margin-bottom:8px}
.page-header p{font-size:14px;color:#c7c4d8;max-width:512px;line-height:1.6}
.invite-btn{display:flex;align-items:center;gap:8px;padding:8px 24px;background:#4f46e5;color:#dad7ff;border:none;border-radius:4px;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:all .2s}
.invite-btn:hover{filter:brightness(1.1)}
.invite-btn:active{transform:scale(.95)}
.invite-btn .m{font-size:16px}

.tabs{display:flex;border-bottom:1px solid #464555;margin-bottom:24px}
.tab{padding:12px 24px;border-bottom:2px solid transparent;font-weight:500;color:#c7c4d8;cursor:pointer;transition:all .2s;background:none;border-top:none;border-left:none;border-right:none;font-size:14px}
.tab.active{border-bottom-color:#c3c0ff;color:#c3c0ff;font-weight:700}
.tab:hover{color:#dae2fd}

.table-wrap{background:#171f33;border:1px solid #464555;border-radius:8px;overflow:hidden}
table{width:100%;border-collapse:collapse}
thead{background:#131b2e;border-bottom:1px solid #464555}
th{padding:12px 24px;font-size:11px;font-weight:600;color:#c7c4d8;text-transform:uppercase;letter-spacing:.05em;text-align:left;font-family:'JetBrains Mono',monospace}
tbody tr{border-bottom:1px solid rgba(70,69,85,.3);transition:all .2s}
tbody tr:hover{background:rgba(45,52,73,.3)}
tbody td{padding:12px 24px}
.member-cell{display:flex;align-items:center;gap:12px}
.member-avatar{width:40px;height:40px;border-radius:4px;border:1px solid #464555;overflow:hidden}
.member-avatar img{width:100%;height:100%;object-fit:cover}
.member-name{font-size:14px;font-weight:700;color:#dae2fd}
.member-email{font-size:12px;color:#c7c4d8}
select{background:#131b2e;border:1px solid #464555;border-radius:4px;padding:4px 8px;font-size:12px;color:#dae2fd;outline:none;cursor:pointer}
select:focus{border-color:#c3c0ff}
.status-dot{display:flex;align-items:center;gap:4px}
.status-dot .dot{width:8px;height:8px;border-radius:50%}
.status-dot .dot.on{background:#89ceff}
.status-dot .dot.off{background:#464555}
.status-dot span{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.badge{font-size:12px;padding:2px 8px;border-radius:4px;font-family:'JetBrains Mono',monospace}
.badge.full{color:#89ceff;background:rgba(137,206,255,.2);border:1px solid rgba(137,206,255,.3)}
.badge.read{color:#c3c0ff;background:rgba(195,192,255,.2);border:1px solid rgba(195,192,255,.3)}
.badge.scoped{color:#c7c4d8;background:rgba(45,52,73,.4);border:1px solid rgba(70,69,85,.3)}

.perms{margin-top:48px}
.perms h2{font-size:24px;line-height:32px;font-weight:600;margin-bottom:24px}
.perms-grid{display:grid;grid-template-columns:1fr;gap:24px}
@media(min-width:768px){.perms-grid{grid-template-columns:repeat(2,1fr)}}
.perm-card{background:#131b2e;border:1px solid #464555;padding:24px;border-radius:8px}
.perm-item{display:flex;justify-content:space-between;align-items:flex-start}
.perm-item+.perm-item{margin-top:24px}
.perm-item h4{font-size:14px;font-weight:700;color:#dae2fd;margin-bottom:4px}
.perm-item p{font-size:12px;color:#c7c4d8}
.toggle{position:relative;width:44px;height:24px;cursor:pointer;flex-shrink:0}
.toggle input{opacity:0;width:0;height:0}
.toggle-track{position:absolute;inset:0;background:#2d3449;border-radius:999px;transition:all .2s}
.toggle input:checked+.toggle-track{background:#c3c0ff}
.toggle-thumb{position:absolute;top:2px;left:2px;width:20px;height:20px;background:#fff;border-radius:50%;transition:all .2s}
.toggle input:checked~.toggle-thumb{transform:translateX(20px)}

.modal-overlay{display:none;position:fixed;inset:0;z-index:100;background:rgba(11,19,38,.8);backdrop-filter:blur(4px);align-items:center;justify-content:center}
.modal-overlay.show{display:flex}
.modal{background:#171f33;border:1px solid #464555;border-radius:8px;width:100%;max-width:448px;padding:24px;box-shadow:0 25px 50px rgba(0,0,0,.5)}
.modal-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.modal-head h3{font-size:24px;line-height:32px;font-weight:600}
.modal-head .m{font-size:20px;color:#c7c4d8;cursor:pointer}
.modal-head .m:hover{color:#dae2fd}
.form-group{margin-bottom:24px}
.form-group label{display:block;font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;text-transform:uppercase;margin-bottom:4px;font-family:'JetBrains Mono',monospace}
.form-group input{width:100%;background:#131b2e;border:1px solid #464555;border-radius:4px;padding:8px;font-size:14px;color:#dae2fd;outline:none}
.form-group input:focus{border-color:#c3c0ff}
.role-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.role-btn{border:1px solid #464555;background:rgba(45,52,73,.1);padding:8px;border-radius:4px;font-size:12px;color:#dae2fd;text-align:center;cursor:pointer;transition:all .2s;font-family:'JetBrains Mono',monospace}
.role-btn.active{border-color:#c3c0ff;background:#4f46e5;color:#fff}
.role-btn:hover{background:rgba(45,52,73,.3)}
.modal-actions{display:flex;gap:16px;margin-top:32px}
.modal-actions button{flex:1;padding:8px;border-radius:4px;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:all .2s}
.modal-cancel{background:transparent;border:1px solid #464555;color:#c7c4d8}
.modal-cancel:hover{background:rgba(45,52,73,.5)}
.modal-send{background:#4f46e5;border:none;color:#dad7ff}
.modal-send:hover{filter:brightness(1.1)}
.modal-send:active{transform:scale(.95)}
</style>
</head>
<body>
<div class="layout">
<header class="nav">
<div class="nav-l">
<a href="/" style="text-decoration:none;color:#dae2fd"><span class="nav-brand">BuildTogether</span></a>
<div class="nav-links">
<a href="/">IDE</a>
<a href="/dashboard">Projects</a>
<a class="active" href="/team">Team</a>
<a href="/landing">Landing</a>
</div>
</div>
</div>
<div class="nav-r">
<div class="nav-search"><input type="text" placeholder="Search team..."><span class="m material-symbols-outlined">search</span></div>
<button class="nav-icon"><span class="m material-symbols-outlined">notifications</span></button>
<button class="nav-icon"><span class="m material-symbols-outlined">history</span></button>
<div class="nav-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBfxoOblZFz0n6QYj8yiPRDsWrKy7FeXCWs9cPVcVF6g5BbqSAYwoMK8MtWwsHrU4O2dkBD1svAdZslTfWHsA1XoOYA9_-Qli7HoLL4duPzYd5I8lZBtkx2lxkqAAoborUJYSvxGDtIfCQ5Eq1ujyFMBkX8S0XgNH0n9NEItPACgak1ICfMLzKfYk8yYayPuhbKw3ZvHWkGRkmItJ9BEOOR3qjsXyxxbBYGAfKOYNcXeDlGQ5GSvhlj7A" alt=""></div>
</div>
</header>

<div class="body">
<aside class="sidebar">
<div class="sidebar-top">
<div class="sidebar-head">
<div class="sidebar-head-label"><div class="icon"><span class="m material-symbols-outlined">hub</span></div><span>Workspace</span></div>
<div class="sidebar-head-sub">build-together-main</div>
</div>
<nav class="sidebar-nav">
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">folder_open</span><span>Explorer</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">search</span><span>Search</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">account_tree</span><span>Source Control</span></div>
<div class="sidebar-nav-item active"><span class="m material-symbols-outlined" style="font-variation-settings:'FILL' 1">groups</span><span>Team Admin</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">bug_report</span><span>Debugger</span></div>
</nav>
</div>
<div class="sidebar-bottom">
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">settings</span><span>Settings</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">person</span><span>Account</span></div>
</div>
</aside>

<main class="main">
<div class="main-inner">
<div class="page-header">
<div><h1>Team Management</h1><p>Manage your organization's members, control roles, and audit technical permissions across all active repositories.</p></div>
<button class="invite-btn" onclick="document.getElementById('inviteModal').classList.add('show')"><span class="m material-symbols-outlined">person_add</span>Invite Member</button>
</div>

<div class="tabs">
<button class="tab active">Members</button>
<button class="tab">Security & Permissions</button>
<button class="tab">Activity Log</button>
</div>

<div class="table-wrap">
<table>
<thead><tr><th>Member</th><th>Role</th><th>Status</th><th>Access</th><th></th></tr></thead>
<tbody>
<tr>
<td><div class="member-cell"><div class="member-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAqp1yzz8NZ9F69kmzqz2Bw2sBp8965tvFMujU0RMFQDR5f4vR2GQs-bi0yfj6NlgzwznorerY896qhVdu8T-3M64nFrcdQX8roanE9Dhlspjn5hGIGSmym-S-vI2lex4UULTYYeH28OF9z4qN546GVN_DrpvbOQMkPi38DyLkXzubfsLy3XdIgk_Bf5YWKWvKmUvigPxw8xeCi7uy0U5_LopLr2YuJiTl6ju3dRkczM1hUQnSWolMfkg" alt=""></div><div><div class="member-name">Alex Rivera</div><div class="member-email">alex@buildtogether.io</div></div></div></td>
<td><select><option selected>Owner</option><option>Admin</option><option>Developer</option></select></td>
<td><div class="status-dot"><div class="dot on"></div><span style="color:#dae2fd">Active</span></div></td>
<td><span class="badge full">Full-Access</span></td>
<td><button class="nav-icon"><span class="m material-symbols-outlined">more_vert</span></button></td>
</tr>
<tr>
<td><div class="member-cell"><div class="member-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuATwfmJ95NMOKUhx4SX7z6cUUkKxgVNAyhdQuS6w_Zkxc008Qz5fgdhFtYhn5Phg5r7VmQLkzpOAj7Zn3g3kVmvaNtxdrUXq1QAmYWW-tWIgctFlUI--gSG8F89RRMR1dYYHdlGWR-GS74iDxGIvdEyhn184najmt7hD1ZJZECouf8ozD8EX56bbmvfvlE2pZqABssWNfseuyllfMYC718m8K2RBldGqgwCRFSua_K5IapjeEviC-iAQQ" alt=""></div><div><div class="member-name">Elena Vance</div><div class="member-email">e.vance@buildtogether.io</div></div></div></td>
<td><select><option>Owner</option><option selected>Admin</option><option>Developer</option></select></td>
<td><div class="status-dot"><div class="dot on"></div><span style="color:#dae2fd">Active</span></div></td>
<td><span class="badge read">Repo-Read</span></td>
<td><button class="nav-icon"><span class="m material-symbols-outlined">more_vert</span></button></td>
</tr>
<tr>
<td><div class="member-cell"><div class="member-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCYUMStouvoT5Eppt_1tI7fxbcIbM5z1G7XKF3aNgUYsarPIAAZ82ERRdy034zkI8WnBImqh4em0NOYT2AtXr_qkJFismMxDuedKcBU6yGylai4Rkjg-nZr-FmmHx0dDigCe2FJDd8ACTAuqABVd1dbg2YvjMxVZDMulkE3Zbvf9ieRPWUsM2_moZAsH2-gKmPeLffnQdAWYDihhN34fYJMuVJC6IMATifyg3iU0jJddUPpzPyjW1TimQ" alt=""></div><div><div class="member-name">Marcus Chen</div><div class="member-email">marcus@buildtogether.io</div></div></div></td>
<td><select><option>Owner</option><option>Admin</option><option selected>Developer</option></select></td>
<td><div class="status-dot"><div class="dot off"></div><span style="color:#c7c4d8">Offline</span></div></td>
<td><span class="badge scoped">Scoped</span></td>
<td><button class="nav-icon"><span class="m material-symbols-outlined">more_vert</span></button></td>
</tr>
</tbody>
</table>
</div>

<div class="perms">
<h2>Default Repository Permissions</h2>
<div class="perms-grid">
<div class="perm-card">
<div class="perm-item"><div><h4>Repository-Level Write</h4><p>Allow administrators to push directly to production branches.</p></div><label class="toggle"><input type="checkbox" checked><div class="toggle-track"></div><div class="toggle-thumb"></div></label></div>
<div class="perm-item"><div><h4>Force Code Review</h4><p>Require at least 2 approvals for all pull requests.</p></div><label class="toggle"><input type="checkbox" checked><div class="toggle-track"></div><div class="toggle-thumb"></div></label></div>
</div>
<div class="perm-card">
<div class="perm-item"><div><h4>External Collaborators</h4><p>Permit adding non-org users to specific private repos.</p></div><label class="toggle"><input type="checkbox"><div class="toggle-track"></div><div class="toggle-thumb"></div></label></div>
<div class="perm-item"><div><h4>API Token Creation</h4><p>Allows team members to generate personal access tokens.</p></div><label class="toggle"><input type="checkbox"><div class="toggle-track"></div><div class="toggle-thumb"></div></label></div>
</div>
</div>
</div>
</div>
</main>
</div>

<footer style="display:flex;align-items:center;justify-content:space-between;padding:8px 48px;width:100%;background:#060e20;border-top:1px solid #464555;z-index:40;flex-shrink:0">
<span style="font-size:14px;color:#c7c4d8;opacity:.6">© 2024 BuildTogether. Technical Precision.</span>
<div class="footer-links">
<a href="#">Privacy</a><a href="#">Terms</a><a href="#">Documentation</a><a href="#">API</a><a href="#">Status</a>
</div>
</footer>
</div>

<div class="modal-overlay" id="inviteModal">
<div class="modal">
<div class="modal-head"><h3>Invite Member</h3><span class="m material-symbols-outlined" onclick="document.getElementById('inviteModal').classList.remove('show')">close</span></div>
<div class="form-group"><label>Email Address</label><input type="email" placeholder="dev@company.com"></div>
<div class="form-group"><label>Select Role</label>
<div class="role-grid">
<div class="role-btn">Owner</div>
<div class="role-btn active">Admin</div>
<div class="role-btn">Developer</div>
</div>
</div>
<div class="modal-actions">
<button class="modal-cancel" onclick="document.getElementById('inviteModal').classList.remove('show')">Cancel</button>
<button class="modal-send">Send Invitation</button>
</div>
</div>
</div>
<script>
document.querySelectorAll('.role-btn').forEach(function(b){b.addEventListener('click',function(){document.querySelectorAll('.role-btn').forEach(function(x){x.classList.remove('active')});this.classList.add('active')})});
document.addEventListener('keydown',function(e){if(e.key==='Escape')document.getElementById('inviteModal').classList.remove('show')});
</script>
</body></html>"""

# ─── IDE PAGE ───
IDE = COMMON + """
<style>
.layout{display:flex;flex-direction:column;height:100vh;overflow:hidden}
.nav{display:flex;justify-content:space-between;align-items:center;height:40px;padding:0 16px;width:100%;z-index:50;background:#0b1326;border-bottom:1px solid #464555;flex-shrink:0}
.nav-l{display:flex;align-items:center;gap:16px}
.nav-logo{display:flex;align-items:center;gap:8px}
.nav-logo .icon{width:24px;height:24px;background:#4f46e5;border-radius:4px;display:flex;align-items:center;justify-content:center}
.nav-logo .icon .m{font-size:18px;color:#c3c0ff}
.nav-logo .name{font-size:18px;font-weight:700;color:#dae2fd;letter-spacing:-.01em}
.nav-links{display:none;align-items:center;gap:8px}
@media(min-width:768px){.nav-links{display:flex}}
.nav-links a{font-size:13px;color:#c7c4d8;padding:4px 12px;border-radius:6px;transition:all .2s}
.nav-links a:hover{background:rgba(45,52,73,.5)}
.nav-links a.active{background:#222a3d;color:#dae2fd;font-weight:600}
.nav-r{display:flex;align-items:center;gap:8px}
.run-group{display:flex;background:#131b2e;border-radius:8px;padding:2px;border:1px solid #464555}
.run-btn{display:flex;align-items:center;gap:4px;padding:4px 12px;border-radius:6px;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;border:none;transition:all .2s}
.run-btn.primary{background:#4f46e5;color:#dad7ff}
.run-btn.secondary{background:transparent;color:#c7c4d8}
.run-btn:hover{filter:brightness(1.1)}
.run-btn .m{font-size:16px}
.share-btn{display:flex;align-items:center;gap:4px;padding:6px 12px;border:1px solid #464555;border-radius:8px;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;background:transparent;color:#dae2fd;transition:all .2s}
.share-btn:hover{background:rgba(45,52,73,.5)}
.share-btn .m{font-size:16px}
.nav-icon{background:none;border:none;color:#c7c4d8;padding:6px;border-radius:6px;transition:all .2s;line-height:1}
.nav-icon:hover{background:rgba(45,52,73,.5)}
.nav-icon .m{font-size:20px}
.nav-div{width:1px;height:24px;background:#464555;margin:0 4px}
.nav-avatar{width:32px;height:32px;border-radius:50%;border:1px solid #464555;overflow:hidden;cursor:pointer;transition:all .2s}
.nav-avatar:hover{border-color:#c3c0ff}
.nav-avatar img{width:100%;height:100%;object-fit:cover}

.body{display:flex;flex:1;overflow:hidden}

.act-bar{width:56px;background:#131b2e;border-right:1px solid #464555;display:flex;flex-direction:column;justify-content:space-between;padding:16px 0;align-items:center;flex-shrink:0}
.act-bar-top,.act-bar-bot{display:flex;flex-direction:column;gap:16px;align-items:center;width:100%}
.act-item{width:100%;display:flex;justify-content:center;padding:8px;color:#c7c4d8;cursor:pointer;border-left:2px solid transparent;transition:all .2s}
.act-item:hover{color:#dae2fd}
.act-item.active{border-left-color:#c3c0ff;background:rgba(195,192,255,.05);color:#c3c0ff}
.act-item .m{font-size:24px}

.explorer{width:260px;background:#0b1326;border-right:1px solid #464555;display:none;flex-direction:column;flex-shrink:0}
@media(min-width:768px){.explorer{display:flex}}
.explorer-head{padding:12px 16px;display:flex;justify-content:space-between;align-items:center;height:40px}
.explorer-head span{font-size:10px;font-weight:700;letter-spacing:.15em;color:#c7c4d8;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.explorer-head .m{font-size:16px;color:#c7c4d8;cursor:pointer}
.explorer-body{flex:1;overflow-y:auto}
.tree{list-style:none}
.tree-summary{display:flex;align-items:center;gap:4px;padding:4px 16px;font-size:11px;font-weight:600;color:#c7c4d8;cursor:pointer;transition:background .15s;list-style:none}
.tree-summary:hover{background:#222a3d}
.tree-summary .m{font-size:16px;transition:transform .15s}
.tree[open]>.tree-summary .m{transform:rotate(90deg)}
.tree-c{margin-left:16px;margin-top:4px}
.tree-inner{list-style:none}
.tree-inner-summary{display:flex;align-items:center;gap:6px;padding:4px 12px;font-size:13px;color:#c7c4d8;cursor:pointer;transition:background .15s;list-style:none}
.tree-inner-summary:hover{background:#222a3d}
.tree-inner-summary .fa{font-size:16px;color:rgba(195,192,255,.8);transition:transform .15s}
.tree[open]>.tree-inner-summary .fa{transform:rotate(90deg)}
.tree-inner-c{margin-left:16px;border-left:1px solid rgba(70,69,85,.3)}
.file-item{display:flex;align-items:center;gap:8px;padding:4px 24px;font-size:13px;color:#c7c4d8;cursor:pointer;transition:all .15s;border-left:2px solid transparent}
.file-item:hover{background:#222a3d}
.file-item.active{background:rgba(195,192,255,.1);border-left-color:#c3c0ff;color:#dae2fd}
.file-item .m{font-size:18px}
.file-item .js{color:#89ceff}
.file-item .css{color:#c3c0ff}
.file-item-root{display:flex;align-items:center;gap:8px;padding:4px 12px;font-size:13px;color:#c7c4d8;cursor:pointer;transition:background .15s}
.file-item-root:hover{background:#222a3d}
.file-item-root .m{font-size:18px}

.editor{flex:1;display:flex;flex-direction:column;min-width:0;background:#060e20}
.editor-tabs{display:flex;background:#131b2e;border-bottom:1px solid #464555;height:40px;overflow-x:auto}
.editor-tab{display:flex;align-items:center;gap:8px;padding:0 16px;height:100%;border-right:1px solid #464555;cursor:pointer;white-space:nowrap;border-top:2px solid transparent;font-size:12px;font-family:'JetBrains Mono',monospace}
.editor-tab:hover{opacity:1}
.editor-tab.active{background:#060e20;border-top-color:#c3c0ff;color:#dae2fd}
.editor-tab .m{font-size:16px}
.editor-tab .js{color:#89ceff}
.editor-tab .css{color:#c3c0ff}
.editor-tab .close{font-size:14px;color:#c7c4d8;cursor:pointer;border-radius:4px;line-height:1}
.editor-tab .close:hover{background:#2d3449}
.editor-tab.inactive{opacity:.6}
.editor-tab.inactive:hover{opacity:1}
.editor-bc{display:flex;align-items:center;justify-content:space-between;padding:4px 16px;border-bottom:1px solid #464555;background:rgba(23,31,51,.5)}
.editor-bc-l{display:flex;align-items:center;gap:6px;font-size:11px;color:#c7c4d8}
.editor-bc-l .cur{color:#dae2fd;font-weight:500}
.editor-bc-l .m{font-size:14px}
.ai-toggle{display:flex;align-items:center;gap:4px;padding:2px 8px;background:rgba(79,70,229,.1);border-radius:999px;border:1px solid rgba(79,70,229,.2);cursor:pointer}
.ai-toggle:hover{background:rgba(79,70,229,.2)}
.ai-toggle .m{font-size:14px;color:#c3c0ff}
.ai-toggle span{font-size:10px;font-weight:700;color:#c3c0ff;letter-spacing:.05em;text-transform:uppercase}

.code-area{flex:1;display:flex;font-family:'JetBrains Mono',monospace;font-size:13px;line-height:1.6;overflow:hidden;position:relative}
.line-nums{width:48px;padding:16px 0;text-align:right;padding-right:16px;color:rgba(70,69,85,.4);user-select:none;background:rgba(6,14,32,.8);border-right:1px solid rgba(70,69,85,.1)}
.line-nums .hl{color:#c3c0ff;font-weight:700}
.code-content{flex:1;padding:16px;overflow:auto;white-space:pre;position:relative;background:#060e20}
.code-bg{position:absolute;inset:0;pointer-events:none;opacity:.03;background-image:radial-gradient(#4f46e5 .5px,transparent .5px);background-size:20px 20px}
.kw{color:#c3c0ff;font-weight:600}
.st{color:#89ceff}
.cmt{color:#918fa1;font-style:italic}
.fn{color:#ffb695}
.active-line{background:rgba(79,70,229,.1);border-left:2px solid #4f46e5;display:flex;align-items:center}
.cursor-line{display:inline-block;width:2px;height:20px;background:#c3c0ff;margin-left:4px;animation:blink 1s step-end infinite;vertical-align:middle}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}
.ai-ghost{display:block;padding:4px 16px 4px 12px;margin:4px 0;border-left:2px solid rgba(79,70,229,.2);background:rgba(79,70,229,.05);border-radius:0 8px 8px 0}
.ai-ghost-text{color:rgba(195,192,255,.4);font-style:italic}
.ai-label{display:flex;align-items:center;gap:8px;margin-top:4px}
.ai-label .tag{font-size:10px;background:#4f46e5;color:#dad7ff;padding:2px 8px;border-radius:4px;font-weight:700}
.ai-label .hint{font-size:10px;color:#c7c4d8}
.cursor{position:absolute;z-index:10;display:flex;flex-direction:column;align-items:flex-start}
.cursor-line-bar{width:2px;height:20px}
.cursor-name{font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;white-space:nowrap}
.cursor.c1 .cursor-line-bar{background:#c3c0ff}
.cursor.c1 .cursor-name{background:#c3c0ff;color:#0f0069}
.cursor.c2 .cursor-line-bar{background:#89ceff}
.cursor.c2 .cursor-name{background:#89ceff;color:#001e2f}

.terminal{height:192px;background:#0b1326;border-top:1px solid #464555;display:flex;flex-direction:column}
.terminal-head{display:flex;align-items:center;justify-content:space-between;padding:0 16px;border-bottom:1px solid #464555;background:#171f33;min-height:36px}
.terminal-tabs{display:flex;gap:24px}
.terminal-tab{position:relative;padding:8px 0;font-size:11px;font-weight:700;color:#c7c4d8;cursor:pointer;text-transform:uppercase;letter-spacing:.05em;transition:color .15s;font-family:'JetBrains Mono',monospace}
.terminal-tab:hover{color:#dae2fd}
.terminal-tab.active{color:#dae2fd}
.terminal-tab.active::after{content:'';position:absolute;bottom:0;left:0;width:100%;height:2px;background:#c3c0ff}
.terminal-actions{display:flex;gap:4px}
.terminal-actions .m{font-size:18px;color:#c7c4d8;padding:4px;border-radius:4px;cursor:pointer;transition:all .15s;line-height:1}
.terminal-actions .m:hover{background:#2d3449}
.terminal-body{flex:1;padding:16px;font-family:'JetBrains Mono',monospace;font-size:12px;line-height:18px;overflow-y:auto}
.terminal-body .time{color:#c7c4d8}
.terminal-body .ok{color:#89ceff;font-weight:700}
.terminal-body .link{color:#c3c0ff;text-decoration:underline;cursor:pointer}
.terminal-body .prompt{color:#c3c0ff;font-weight:700}
.terminal-body .branch{color:#89ceff;font-weight:700}
.terminal-body .feat{color:#ffb695}
.terminal-body .dim{color:rgba(199,196,216,.6)}
.terminal-body .cursor-block{display:inline-block;width:6px;height:16px;background:rgba(195,192,255,.6);animation:pulse 1s step-end infinite;vertical-align:middle}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

.collab{width:260px;background:#0b1326;border-left:1px solid #464555;display:none;flex-direction:column}
@media(min-width:1024px){.collab{display:flex}}
.collab-section{padding:16px;border-bottom:1px solid #464555;background:#131b2e}
.collab-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.collab-head span{font-size:10px;font-weight:700;letter-spacing:.2em;color:#c7c4d8;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.collab-online{font-size:10px;padding:2px 6px;background:rgba(74,222,128,.1);color:#4ade80;font-weight:700;border-radius:4px}
.collab-list{display:flex;flex-direction:column;gap:12px}
.collab-item{display:flex;align-items:center;justify-content:space-between;cursor:pointer}
.collab-item.inactive{opacity:.6}
.collab-left{display:flex;align-items:center;gap:12px}
.collab-avatar{position:relative;width:36px;height:36px;border-radius:50%;overflow:hidden;flex-shrink:0}
.collab-avatar img{width:100%;height:100%;object-fit:cover;border-radius:50%;padding:2px}
.collab-avatar.purple{border:2px solid #c3c0ff}
.collab-avatar.blue{border:2px solid #89ceff}
.collab-avatar.orange{border:2px solid #ffb695}
.collab-status{position:absolute;bottom:0;right:0;width:10px;height:10px;border-radius:50%;border:2px solid #0b1326}
.collab-status.on{background:#4ade80}
.collab-status.away{background:#eab308}
.collab-name{font-size:12px;font-weight:700;color:#dae2fd}
.collab-role{font-size:10px}
.collab-role.host{color:#c3c0ff}
.collab-role.default{color:#c7c4d8}
.collab-mic{font-size:18px;flex-shrink:0}
.collab-mic.on{color:#c3c0ff}
.collab-mic.off{color:rgba(199,196,216,.4)}

.chat{flex:1;display:flex;flex-direction:column;min-height:0;background:#0b1326}
.chat-head{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-bottom:1px solid #464555}
.chat-head span{font-size:10px;font-weight:700;letter-spacing:.2em;color:#c7c4d8;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.chat-head .m{font-size:16px;color:#c7c4d8;cursor:pointer;padding:4px;border-radius:4px;transition:background .15s}
.chat-head .m:hover{background:#2d3449}
.chat-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:16px}
.chat-msg{display:flex;flex-direction:column;gap:6px}
.chat-msg-head{display:flex;align-items:center;gap:8px}
.chat-msg-name{font-size:11px;font-weight:700}
.chat-msg-name.purple{color:#c3c0ff}
.chat-msg-name.blue{color:#89ceff}
.chat-msg-name.orange{color:#ffb695}
.chat-msg-time{font-size:9px;color:rgba(199,196,216,.6)}
.chat-msg-body{font-size:12px;line-height:1.5;background:#222a3d;padding:12px;border-radius:12px 12px 12px 4px;color:#dae2fd;border:1px solid rgba(70,69,85,.5);max-width:90%}
.chat-input{padding:16px;border-top:1px solid #464555;background:#131b2e}
.chat-input-wrap{position:relative}
.chat-input-wrap textarea{width:100%;background:#060e20;border:1px solid #464555;border-radius:12px;padding:12px;padding-bottom:40px;font-size:12px;color:#dae2fd;font-family:'Inter',sans-serif;resize:none;outline:none;transition:all .2s;line-height:1.5}
.chat-input-wrap textarea:focus{border-color:#c3c0ff;box-shadow:0 0 0 2px rgba(195,192,255,.2)}
.chat-input-wrap textarea::placeholder{color:rgba(199,196,216,.4)}
.chat-emojis{position:absolute;left:12px;bottom:10px;display:flex;gap:8px}
.chat-emojis .m{font-size:18px;color:#c7c4d8;padding:4px;border-radius:4px;cursor:pointer;transition:background .15s;line-height:1}
.chat-emojis .m:hover{background:#2d3449}
.chat-send{position:absolute;right:12px;bottom:10px}
.chat-send button{display:flex;align-items:center;gap:6px;padding:4px 12px;background:#4f46e5;color:#dad7ff;border:none;border-radius:8px;font-size:11px;font-weight:700;cursor:pointer;transition:all .2s;font-family:'JetBrains Mono',monospace}
.chat-send button:hover{filter:brightness(1.1)}
.chat-send button:active{transform:scale(.95)}
.chat-send .m{font-size:14px}

.statusbar{height:24px;background:#4f46e5;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font-size:10px;font-weight:700;color:#dad7ff;z-index:50;flex-shrink:0}
.statusbar-l,.statusbar-r{display:flex;align-items:center;height:100%}
.statusbar-item{display:flex;align-items:center;gap:6px;padding:0 12px;height:100%;cursor:pointer;transition:background .1s;border-right:1px solid rgba(255,255,255,.1);text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.statusbar-item:hover{background:rgba(255,255,255,.1)}
.statusbar-item .m{font-size:14px}
.statusbar-item .dim{color:rgba(255,255,255,.6)}
.statusbar-info{display:flex;align-items:center;gap:16px;padding:0 16px;border-left:1px solid rgba(255,255,255,.1);height:100%;text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.statusbar-build{display:flex;align-items:center;gap:6px;padding:0 16px;height:100%;border-left:1px solid rgba(255,255,255,.1);cursor:pointer;background:rgba(74,222,128,.3);text-transform:uppercase;font-family:'JetBrains Mono',monospace}
.statusbar-build:hover{background:rgba(74,222,128,.4)}
.statusbar-build .m{font-size:14px;color:#86efac}
</style>
</head>
<body>
<div class="layout">
<header class="nav">
<div class="nav-l">
<a href="/" class="nav-logo" style="text-decoration:none"><div class="icon"><span class="m material-symbols-outlined">bolt</span></div><span class="name">BuildTogether</span></a>
<div class="nav-links">
<a class="active" href="/">IDE</a>
<a href="/dashboard">Projects</a>
<a href="/team">Team</a>
<a href="/landing">Landing</a>
</div>
</div>
<div class="nav-r">
<div class="run-group"><button class="run-btn primary"><span class="m material-symbols-outlined">play_arrow</span>Run</button><button class="run-btn secondary"><span class="m material-symbols-outlined">bug_report</span>Debug</button></div>
<button class="share-btn"><span class="m material-symbols-outlined">ios_share</span>Share</button>
<div class="nav-div"></div>
<button class="nav-icon"><span class="m material-symbols-outlined">notifications</span></button>
<button class="nav-icon"><span class="m material-symbols-outlined">history</span></button>
<button class="nav-icon"><span class="m material-symbols-outlined">search</span></button>
<div class="nav-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDoDeRlFy-lIt8-Grb7UF8PaCm-EWEFMTgVFqR3Bho_tYpUJOrBvTjRwR6FOZZJyB3Aet8NN-EzZdhoYls1IFk_tZw4oe1XazYU_GeH1oPIUCsYS0gRC0ENmd1nfOg5t9EV7PU6C-sPlyp-Fws_AsKKbJRYVk2e_6WqzLL9QsCIvw0if9h-qqur_yWh73oPIp2hyMhohtFAN65xvJ7VfX8VW307COf8MRTntTFLGqJNXdKxxoVUfiSVFQ" alt=""></div>
</div>
</header>

<div class="body">
<aside class="act-bar">
<div class="act-bar-top">
<div class="act-item active"><span class="m material-symbols-outlined">folder</span></div>
<div class="act-item"><span class="m material-symbols-outlined">search</span></div>
<div class="act-item"><span class="m material-symbols-outlined">account_tree</span></div>
<div class="act-item"><span class="m material-symbols-outlined">terminal</span></div>
<div class="act-item"><span class="m material-symbols-outlined">extension</span></div>
</div>
<div class="act-bar-bot">
<div class="act-item"><span class="m material-symbols-outlined">settings</span></div>
<div class="act-item"><span class="m material-symbols-outlined">account_circle</span></div>
</div>
</aside>

<div class="explorer">
<div class="explorer-head"><span>Explorer</span><span class="m material-symbols-outlined">more_horiz</span></div>
<div class="explorer-body">
<details class="tree" open>
<summary class="tree-summary"><span class="m material-symbols-outlined">chevron_right</span>Build-Together-Main</summary>
<div class="tree-c">
<details class="tree" open>
<summary class="tree-inner-summary"><span class="fa material-symbols-outlined">chevron_right</span><span class="fa material-symbols-outlined" style="color:rgba(195,192,255,.8)">folder</span>src</summary>
<div class="tree-inner-c">
<div class="file-item"><span class="js material-symbols-outlined">javascript</span>App.js</div>
<div class="file-item active"><span class="js material-symbols-outlined">javascript</span>Editor.js</div>
<div class="file-item"><span class="css material-symbols-outlined">css</span>styles.css</div>
</div>
</details>
<div class="file-item-root"><span class="m material-symbols-outlined" style="color:#ffb695">description</span>package.json</div>
<div class="file-item-root"><span class="m material-symbols-outlined" style="color:rgba(199,196,216,.6)">info</span>README.md</div>
</div>
</details>
</div>
</div>

<main class="editor">
<div class="editor-tabs">
<div class="editor-tab active"><span class="js material-symbols-outlined">javascript</span>Editor.js<span class="close material-symbols-outlined">close</span></div>
<div class="editor-tab inactive"><span class="js material-symbols-outlined">javascript</span>App.js<span class="close material-symbols-outlined">close</span></div>
<div class="editor-tab inactive"><span class="css material-symbols-outlined">css</span>styles.css<span class="close material-symbols-outlined">close</span></div>
</div>
<div class="editor-bc">
<div class="editor-bc-l"><span>src</span><span class="m material-symbols-outlined">chevron_right</span><span class="cur">Editor.js</span></div>
<div class="ai-toggle"><span class="m material-symbols-outlined">smart_toy</span><span>AI Pilot Active</span></div>
</div>
<div class="code-area">
<div class="line-nums">1<br>2<br>3<br>4<br>5<br>6<br>7<br><span class="hl">8</span><br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20</div>
<div class="code-content">
<div class="code-bg"></div>
<div><span class="kw">import</span> React, { useState, useEffect } <span class="kw">from</span> <span class="st">'react'</span>;</div>
<div><span class="kw">import</span> { Workspace, Collaboration } <span class="kw">from</span> <span class="st">'@build/core'</span>;</div>
<div style="margin-top:16px"><span class="cmt">// Initialize the main collaboration context</span></div>
<div><span class="kw">const</span> Editor = () =&gt; {</div>
<div>    <span class="kw">const</span> [state, setState] = useState(<span class="kw">null</span>);</div>
<div class="active-line">    <span class="kw">const</span> [users, setUsers] = useState([]); <span class="cursor-line"></span></div>
<div class="ai-ghost"><span class="ai-ghost-text">    useEffect(() =&gt; {</span><br><span class="ai-ghost-text">        const session = Collaboration.start();</span><br><span class="ai-ghost-text">        return () =&gt; session.end();</span><br><span class="ai-ghost-text">    }, []);</span>
<div class="ai-label"><span class="tag">Tab to accept</span><span class="hint">AI Suggestion</span></div></div>
<div>    <span class="fn">useEffect</span>(() =&gt; {</div>
<div>        <span class="kw">const</span> sync = <span class="kw">async</span> () =&gt; {</div>
<div>            <span class="kw">await</span> Workspace.<span class="fn">connect</span>({</div>
<div>                id: <span class="st">'main-workspace'</span>,</div>
<div>                mode: <span class="st">'collaborative'</span></div>
<div>            });</div>
<div>        };</div>
<div>        <span class="fn">sync</span>();</div>
<div>    }, []);</div>
<div style="margin-top:16px">    <span class="kw">return</span> (</div>
<div>        &lt;<span class="fn">Container</span>&gt;</div>
<div>            &lt;<span class="fn">CollaborationLayer</span> /&gt;</div>
<div>            &lt;<span class="fn">CodeSurface</span> /&gt;</div>
<div>        &lt;/<span class="fn">Container</span>&gt;</div>
<div>    );</div>
<div>};</div>
<div style="margin-top:16px"><span class="kw">export default</span> Editor;</div>
<div class="cursor c1" style="left:240px;top:144px"><div class="cursor-line-bar"></div><div class="cursor-name">Alex</div></div>
<div class="cursor c2" style="left:380px;top:320px"><div class="cursor-line-bar"></div><div class="cursor-name">Sam</div></div>
</div></div>

<div class="terminal">
<div class="terminal-head">
<div class="terminal-tabs">
<div class="terminal-tab active">Terminal</div>
<div class="terminal-tab">Output</div>
<div class="terminal-tab">Debug Console</div>
</div>
<div class="terminal-actions"><span class="m material-symbols-outlined">add</span><span class="m material-symbols-outlined">delete</span><span class="m material-symbols-outlined">close</span></div>
</div>
<div class="terminal-body">
<div style="display:flex;align-items:center;gap:8px;margin-bottom:4px"><span class="dim">[10:48:22]</span><span style="color:#c7c4d8">Starting development server...</span></div>
<div style="color:#c7c4d8">build-together-main@1.0.0 start /workspace</div>
<div style="color:#c7c4d8">react-scripts start</div>
<div class="ok" style="margin-top:8px;display:flex;align-items:center;gap:8px"><span class="m material-symbols-outlined" style="font-size:16px">check_circle</span>Compiled successfully!</div>
<div style="margin-top:8px;color:#c7c4d8">Project is running at <span class="link">http://localhost:3000</span></div>
<div style="margin-top:12px;display:flex;align-items:center;gap:8px"><span class="prompt">$</span><span class="branch">main</span><span style="color:#c7c4d8">git:(</span><span class="feat">feature/collab</span><span style="color:#c7c4d8">)</span><span class="cursor-block"></span></div>
</div>
</div>
</main>

<div class="collab">
<div class="collab-section">
<div class="collab-head"><span>Collaborators</span><span class="collab-online">3 ONLINE</span></div>
<div class="collab-list">
<div class="collab-item">
<div class="collab-left">
<div class="collab-avatar purple"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuCwqEvXaWoM_C-jE8sBx6crXYAS-em9HLv3cCj7Vv38FnqQdmPsFuAWKRbblKcjuwGJwJNNh7xCePjhj46w-lC4dcUytf3YXXdQMEjD3tasR47EcJyTdRQEeOHSCZTMUj6dhSNUWQO973hblT2FLBqiaD9LFlJ35eE9lYyq2-cVUsJo_YOpUF44wbCIGM0xaW9LUF5sSaUHISkOwvfsqvpT-IK-gIIAxktBBSHh0NOVt1GjUIN7hK99SQ" alt=""><div class="collab-status on"></div></div>
<div><div class="collab-name">Alex (Host)</div><div class="collab-role host">Editing Editor.js</div></div>
</div>
<span class="collab-mic on material-symbols-outlined">mic</span>
</div>
<div class="collab-item inactive">
<div class="collab-left">
<div class="collab-avatar blue"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuDEI9ru1xRHxaPhneDnV7W1o_J6cXnTRiq_4A8T0thYDyRmP9KCoztlPf1vpOqpPIu3E2mbrznucIs8LZ2AyEi24kVL2PG7PrSqnpGKQXqSVorElxGAZnld7UbqXW3niIOh_5nGqMhoa8aVD1VF9AsMccdR1OSr-SJzk_Cp0twwSvwBEPMtN-n4Ckq4zvojNabIJDf0ugbccnorMLn11ge6eiv3a6nycQcx9_ATvTNH--Ayj_MoQORqSw" alt=""><div class="collab-status on"></div></div>
<div><div class="collab-name">Sam</div><div class="collab-role default">Viewing App.js</div></div>
</div>
<span class="collab-mic off material-symbols-outlined">mic_off</span>
</div>
<div class="collab-item" style="opacity:.6">
<div class="collab-left">
<div class="collab-avatar orange"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuByiqndS4wkuKEE4OcgMuJDQVKLy9sOh1WmiqJbgORNSbDREJxjTnSiD-eTGjeUi7VSy4Oj1ViP630EYKrRhgN_7Ns-8AoPbHeW6coBedqUEwhUN5S5KwHlds85iYKJSvJZGZYloLSRV_dpfJcbmvYnvuSYG_15sMiRbE3KdlFXlwvCSAF1UgyLclWejlPNya-iJo6zNH2o6y_7oeXcxhqt73gWqIjvHO2tFjT-rIKQNTPVsH1WGUXQSw" alt=""><div class="collab-status away"></div></div>
<div><div class="collab-name">Jordan</div><div class="collab-role default">Idle &bull; 5m</div></div>
</div>
<span class="collab-mic off material-symbols-outlined">mic_off</span>
</div>
</div>
</div>
<div class="chat">
<div class="chat-head"><span>Team Chat</span><span class="m material-symbols-outlined">settings</span></div>
<div class="chat-messages">
<div class="chat-msg"><div class="chat-msg-head"><span class="chat-msg-name purple">Alex</span><span class="chat-msg-time">10:42 AM</span></div><div class="chat-msg-body">Just updated the CollaborationLayer logic. Can you guys check line 15?</div></div>
<div class="chat-msg"><div class="chat-msg-head"><span class="chat-msg-name blue">Sam</span><span class="chat-msg-time">10:43 AM</span></div><div class="chat-msg-body">Looks clean. I'll test the sync now.</div></div>
<div class="chat-msg"><div class="chat-msg-head"><span class="chat-msg-name orange">Jordan</span><span class="chat-msg-time">10:45 AM</span></div><div class="chat-msg-body">Wait, are we handling the WebSocket disconnect on line 18?</div></div>
</div>
<div class="chat-input">
<div class="chat-input-wrap">
<textarea placeholder="Message the team..." rows="2"></textarea>
<div class="chat-emojis"><span class="m material-symbols-outlined">sentiment_satisfied</span><span class="m material-symbols-outlined">attach_file</span></div>
<div class="chat-send"><button>Send<span class="m material-symbols-outlined" style="font-size:14px">send</span></button></div>
</div>
</div>
</div>
</div>

</div>

<footer class="statusbar">
<div class="statusbar-l">
<div class="statusbar-item"><span class="m material-symbols-outlined">account_tree</span>feature/collab</div>
<div class="statusbar-item"><span class="m material-symbols-outlined">sync</span>Synced</div>
<div class="statusbar-item"><span class="m material-symbols-outlined">info</span><span class="dim">Workspace Ready</span></div>
</div>
<div class="statusbar-r">
<div class="statusbar-info"><span>Ln 8, Col 32</span><span>Spaces: 4</span><span>UTF-8</span></div>
<div class="statusbar-build"><span class="m material-symbols-outlined">check_circle</span><span>Build Passed</span></div>
</div>
</footer>
</div>
<script>
document.querySelectorAll('.file-item,.file-item-root').forEach(function(i){i.addEventListener('click',function(){document.querySelectorAll('.file-item,.file-item-root').forEach(function(x){x.classList.remove('active')});this.classList.add('active')})});
document.querySelectorAll('.editor-tab').forEach(function(t){t.addEventListener('click',function(){document.querySelectorAll('.editor-tab').forEach(function(x){x.classList.remove('active');x.classList.add('inactive')});this.classList.add('active');this.classList.remove('inactive')})});
document.querySelectorAll('.terminal-tab').forEach(function(t){t.addEventListener('click',function(){document.querySelectorAll('.terminal-tab').forEach(function(x){x.classList.remove('active')});this.classList.add('active')})});
document.querySelectorAll('.act-item').forEach(function(i){i.addEventListener('click',function(){document.querySelectorAll('.act-item').forEach(function(x){x.classList.remove('active')});this.classList.add('active')})});
</script>
</body></html>"""

# ─── DASHBOARD PAGE ───
DASHBOARD = COMMON + """
<style>
.layout{display:flex;flex-direction:column;height:100vh;overflow:hidden}
.nav{display:flex;justify-content:space-between;align-items:center;height:40px;padding:0 16px;width:100%;position:fixed;top:0;z-index:50;background:#0b1326;border-bottom:1px solid #464555}
.nav-l{display:flex;align-items:center;gap:24px}
.nav-brand{font-size:24px;font-weight:700;color:#dae2fd;letter-spacing:-.01em}
.nav-links{display:none;align-items:center;gap:8px}
@media(min-width:768px){.nav-links{display:flex}}
.nav-links a{font-size:11px;font-weight:600;color:#c7c4d8;padding:4px 8px;border-radius:4px;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:all .2s;text-transform:uppercase}
.nav-links a:hover{background:rgba(45,52,73,.5)}
.nav-links a.active{color:#c3c0ff;border-bottom:2px solid #c3c0ff}
.nav-r{display:flex;align-items:center;gap:8px}
.nav-search{position:relative}
.nav-search input{background:#131b2e;border:1px solid #464555;border-radius:8px;padding:4px 32px 4px 32px;font-size:12px;color:#dae2fd;outline:none;width:192px;transition:all .2s;font-family:'JetBrains Mono',monospace}
.nav-search input:focus{border-color:#c3c0ff}
.nav-search .m{position:absolute;left:8px;top:50%;transform:translateY(-50%);font-size:16px;color:#c7c4d8}
.nav-icon{background:none;border:none;color:#c7c4d8;padding:4px;border-radius:4px;transition:all .2s;line-height:1}
.nav-icon:hover{background:rgba(45,52,73,.5)}
.nav-icon .m{font-size:20px}
.nav-avatar{width:24px;height:24px;border-radius:50%;border:1px solid #464555;overflow:hidden;margin-left:8px}
.nav-avatar img{width:100%;height:100%;object-fit:cover}

.body{display:flex;flex:1;overflow:hidden;padding-top:40px}
.sidebar{width:260px;background:#131b2e;border-right:1px solid #464555;display:none;flex-direction:column;justify-content:space-between;padding:16px 0;flex-shrink:0}
@media(min-width:1024px){.sidebar{display:flex}}
.sidebar-top{display:flex;flex-direction:column;gap:4px}
.sidebar-head{padding:8px 16px 16px}
.sidebar-head span{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.15em;text-transform:uppercase;font-family:'JetBrains Mono',monospace;display:block;opacity:.6}
.sidebar-head .val{font-size:12px;color:#c3c0ff;font-family:'JetBrains Mono',monospace;display:block;margin-top:4px}
.sidebar-nav{display:flex;flex-direction:column}
.sidebar-nav-item{display:flex;align-items:center;gap:12px;padding:8px 16px;color:#c7c4d8;border-left:2px solid transparent;transition:all .2s;cursor:pointer}
.sidebar-nav-item:hover{background:rgba(45,52,73,.3)}
.sidebar-nav-item.active{border-left-color:#c3c0ff;background:rgba(195,192,255,.1);color:#c3c0ff}
.sidebar-nav-item .m{font-size:20px}
.sidebar-nav-item span{font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.sidebar-bottom{padding-bottom:16px}
.sidebar-bottom .sidebar-nav-item{border-left:none}

.main{flex:1;overflow-y:auto;background:#0b1326;position:relative}
.main-pad{padding:24px;max-width:1280px;margin:0 auto}
.dash-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.dash-header h1{font-size:24px;line-height:32px;letter-spacing:-.01em;font-weight:600}
.dash-header p{font-size:14px;color:#c7c4d8}
.new-project-btn{display:flex;align-items:center;gap:8px;padding:8px 24px;background:#4f46e5;color:#dad7ff;border:none;border-radius:8px;font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:all .2s;box-shadow:0 2px 8px rgba(79,70,229,.2)}
.new-project-btn:hover{filter:brightness(1.1)}
.new-project-btn:active{transform:scale(.95)}
.new-project-btn .m{font-size:20px}

.filter-bar{display:flex;align-items:center;gap:16px;padding:8px 16px;background:#131b2e;border:1px solid #464555;border-radius:8px;margin-bottom:16px}
.filter-bar .m{color:#c7c4d8;font-size:20px}
.filter-bar span{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;white-space:nowrap;cursor:pointer}
.filter-bar span.active{color:#c3c0ff;font-weight:700}
.filter-bar span:hover{color:#dae2fd}

.grid{display:grid;grid-template-columns:1fr;gap:24px}
@media(min-width:1280px){.grid-main{grid-template-columns:repeat(12,1fr)}.grid-8{grid-column:span 8}.grid-4{grid-column:span 4}}
.cards{display:grid;grid-template-columns:1fr;gap:16px}
@media(min-width:768px){.cards{grid-template-columns:repeat(2,1fr)}}

.card-lg{grid-column:1/-1;background:#131b2e;border:1px solid #464555;padding:24px;border-radius:12px;position:relative;overflow:hidden;transition:border-color .3s}
.card-lg:hover{border-color:#c3c0ff}
.card-lg-bg{position:absolute;top:0;right:0;padding:16px;opacity:.1}
.card-lg-bg .m{font-size:96px}
.card-lg-head{display:flex;justify-content:space-between;align-items:flex-start;position:relative;z-index:1}
.card-lg-title{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.card-lg-title .dot{width:8px;height:8px;border-radius:50%;background:#4ade80;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
.card-lg-title h3{font-size:24px;line-height:32px;font-weight:600}
.card-lg p{font-size:14px;color:#c7c4d8;max-width:512px;line-height:1.6;margin-bottom:16px;position:relative;z-index:1}
.card-avatars{display:flex;margin-left:auto}
.card-avatars .av{width:32px;height:32px;border-radius:50%;border:2px solid #131b2e;overflow:hidden;margin-left:-8px}
.card-avatars .av:last-child{display:flex;align-items:center;justify-content:center;background:#2d3449;font-size:10px;font-weight:700;color:#c7c4d8}
.card-avatars .av img{width:100%;height:100%;object-fit:cover}
.card-lg-footer{display:flex;justify-content:space-between;align-items:flex-end;margin-top:24px;padding-top:24px;border-top:1px solid rgba(70,69,85,.3);position:relative;z-index:1}
.sparkline svg{width:192px;height:48px}
.sparkline-label{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;display:block;margin-bottom:8px}
.card-stat{display:flex;align-items:center;gap:32px}
.card-stat-num{font-size:20px;font-weight:700;color:#dae2fd}
.card-stat-label{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}

.card-sm{background:#131b2e;border:1px solid #464555;padding:16px;border-radius:12px;transition:border-color .3s}
.card-sm:hover{border-color:#c3c0ff}
.card-sm-head{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px}
.card-sm h3{font-size:18px;line-height:24px;font-weight:600}
.card-sm .tag{font-size:12px;padding:2px 8px;background:rgba(45,52,73,.4);color:#c7c4d8;border-radius:4px;font-family:'JetBrains Mono',monospace}
.card-sm-row{display:flex;justify-content:space-between;font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;margin-bottom:12px}
.card-sm-footer{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#c7c4d8}
.card-sm-footer .hl{color:#dae2fd;font-weight:700}
.card-sm-sparkline svg{width:100%;height:32px}

.card-empty{border:1px dashed #464555;padding:16px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:8px;cursor:pointer;transition:all .3s}
.card-empty:hover{border-color:#c3c0ff}
.card-empty .m{font-size:48px;color:#c7c4d8;transition:color .3s}
.card-empty:hover .m{color:#c3c0ff}
.card-empty span{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}

.sidebar-panel{background:#131b2e;border:1px solid #464555;border-radius:12px;overflow:hidden}
.sidebar-panel-head{padding:12px 16px;border-bottom:1px solid #464555;display:flex;justify-content:space-between;align-items:center;background:#171f33}
.sidebar-panel-head h3{font-size:11px;font-weight:600;color:#dae2fd;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.sidebar-panel-head .m{font-size:20px;color:#c7c4d8}
.sidebar-panel-body{padding:16px}

.activity-item{display:flex;gap:12px;margin-bottom:16px}
.activity-icon{width:32px;height:32px;border-radius:4px;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.activity-icon .m{font-size:16px}
.activity-icon.primary{background:rgba(195,192,255,.1);color:#c3c0ff}
.activity-icon.tertiary{background:rgba(255,182,149,.2);color:#ffb695}
.activity-icon.error{background:rgba(255,180,171,.1);color:#ffb4ab}
.activity-icon.secondary{background:rgba(137,206,255,.1);color:#89ceff}
.activity-text{font-size:12px;color:#dae2fd;line-height:1.4}
.activity-text .hl{font-weight:700}
.activity-text .link{color:#c3c0ff;font-weight:700}
.activity-meta{font-size:10px;color:#c7c4d8;margin-top:2px}
.view-all-btn{width:100%;padding:8px;text-align:center;font-size:11px;font-weight:600;color:#c7c4d8;border-top:1px solid #464555;cursor:pointer;transition:all .2s;background:transparent;border-left:none;border-right:none;border-bottom:none;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.view-all-btn:hover{background:rgba(45,52,73,.3)}

.deploy-card{padding:8px;background:#060e20;border:1px solid rgba(70,69,85,.3);border-radius:8px;position:relative;overflow:hidden;margin-bottom:12px}
.deploy-card:last-child{margin-bottom:0}
.deploy-bar{position:absolute;left:0;top:0;bottom:0;width:4px}
.deploy-bar.primary{background:#c3c0ff}
.deploy-bar.tertiary{background:#ffb695}
.deploy-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}
.deploy-head .label{font-size:11px;font-weight:600;letter-spacing:.05em;font-family:'JetBrains Mono',monospace}
.deploy-head .label.primary{color:#c3c0ff}
.deploy-head .label.tertiary{color:#ffb695}
.deploy-head .time{font-size:12px;color:#c7c4d8;font-family:'JetBrains Mono',monospace}
.deploy-card p{font-size:13px;font-weight:700;color:#dae2fd}
.deploy-card .status-row{display:flex;align-items:center;gap:4px;margin-top:8px}
.deploy-card .status-row .m{font-size:14px;color:#c7c4d8}
.deploy-card .status-row span{font-size:10px;color:#c7c4d8}

.perf-bar{margin-bottom:12px}
.perf-bar:last-child{margin-bottom:0}
.perf-bar-head{display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px}
.perf-bar-head .name{color:#dae2fd}
.perf-bar-track{height:6px;width:100%;background:#2d3449;border-radius:999px;overflow:hidden}
.perf-bar-fill{height:100%;border-radius:999px}
.perf-bar-fill.primary{background:#c3c0ff}
.perf-bar-fill.secondary{background:#89ceff}
.perf-bar-fill.tertiary{background:#ffb695}

.total-velocity{padding:16px;background:rgba(79,70,229,.1);border-top:1px solid #464555}
.total-velocity .label{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;opacity:.8;display:block;margin-bottom:4px}
.total-velocity .val{font-size:24px;font-weight:700;color:#c3c0ff}
.total-velocity .change{display:flex;justify-content:space-between;align-items:flex-end}
.total-velocity .right{text-align:right}
.total-velocity .right .pct{font-size:12px;font-weight:700;color:#4ade80}
.total-velocity .right .sub{font-size:10px;color:#c7c4d8;font-family:'JetBrains Mono',monospace}

.footer-bar{background:#060e20;border-top:1px solid #464555;padding:8px 48px;display:flex;justify-content:space-between;align-items:center}
.footer-bar span{font-size:14px;color:#c7c4d8;opacity:.6}
.footer-links{display:flex;gap:24px;align-items:center}
.footer-links a{font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace;transition:color .2s}
.footer-links a:hover{color:#c3c0ff}
.footer-links .status{display:flex;align-items:center;gap:4px}
.footer-links .status .dot{width:6px;height:6px;border-radius:50%;background:#4ade80}
</style>
</head>
<body>
<div class="layout">
<header class="nav">
<div class="nav-l">
<a href="/" style="text-decoration:none;color:#dae2fd"><span class="nav-brand">BuildTogether</span></a>
<div class="nav-links">
<a href="/">IDE</a>
<a class="active" href="/dashboard">Projects</a>
<a href="/team">Team</a>
<a href="/landing">Landing</a>
</div>
</div>
<div class="nav-r">
<div class="nav-search"><span class="m material-symbols-outlined">search</span><input type="text" placeholder="Search projects..."></div>
<button class="nav-icon"><span class="m material-symbols-outlined">notifications</span></button>
<button class="nav-icon"><span class="m material-symbols-outlined">history</span></button>
<div class="nav-avatar"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuAs1_-VoDDnaflomw4p82gNPX0siwfoVU_jFpEuHeTqc2bRg07E1TQLud8qmBmCxE7WXRh5UD8iM_Xi4Tst1Q7BlfRWSMSUygaw0SC5vbw3bZNwiytlND_MRNLRuTWc5XvwM-YP_9NL0qa8CkQoROe8VAHVT4vTrDPFpuDVxf8kD8GkpM5JGDtvhc6vkX9ZEowIRVt4rFNflGZYXuJNxrGJTFR9_sq8LsCnGF3jonq9MPO3lIQ1xptzgQ" alt=""></div>
</div>
</header>

<div class="body">
<aside class="sidebar">
<div class="sidebar-top">
<div class="sidebar-head"><span>WORKSPACE</span><span class="val">build-together-main</span></div>
<nav class="sidebar-nav">
<div class="sidebar-nav-item active"><span class="m material-symbols-outlined">folder_open</span><span>Explorer</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">search</span><span>Search</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">account_tree</span><span>Source Control</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">bug_report</span><span>Debugger</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">extension</span><span>Extensions</span></div>
</nav>
</div>
<div class="sidebar-bottom">
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">settings</span><span>Settings</span></div>
<div class="sidebar-nav-item"><span class="m material-symbols-outlined">person</span><span>Account</span></div>
</div>
</aside>

<main class="main">
<div class="main-pad">
<div class="dash-header">
<div><h1>Project Workspace</h1><p>Reviewing active sprints and team velocity across 8 projects.</p></div>
<button class="new-project-btn"><span class="m material-symbols-outlined">add</span>New Project</button>
</div>

<div class="grid grid-main">
<div class="grid-8">
<div class="filter-bar">
<span class="m material-symbols-outlined">filter_list</span>
<span class="active">All Projects</span>
<span>Active Sprints</span>
<span>Backlog</span>
<span>Completed</span>
</div>
<div class="cards">
<div class="card-lg">
<div class="card-lg-bg"><span class="m material-symbols-outlined">terminal</span></div>
<div class="card-lg-head">
<div>
<div class="card-lg-title"><div class="dot"></div><h3>BuildTogether UI Kit</h3></div>
<p>The core design system and component library powering our ecosystem. Currently migrating to Tailwind 4.0 alpha.</p>
</div>
<div class="card-avatars">
<div class="av"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuBjpkTDhonnKEg73F8rTGK_66fKrorhOt-f4uMh-oqTlkUSi1Odv-omM-gaJwQJ8Gmfx2VA9L777cebtbTJqn1RMlCorDHvMmsfwyNyOo_o2Sib0tIw0lScko_afVCihSMvKkNc12O3GGcnEEBdj--Sle2UDY4TIR8PZPVOgcCNwaBbXhtDYKWRC-v2CoRXyDg2g87YJsvRx16whgIOl67JAVFwRPC6054dNP5S7DV1cI0pgV8t_BSN-g" alt=""></div>
<div class="av"><img src="https://lh3.googleusercontent.com/aida-public/AB6AXuASuZHcw60qgSf846i7UX5Rzq3hlnZB4LThnplb0rGiT-zxU63Z5v0-zm1nGe7EmrcksJ_-bin04xZBZHZ8stYuTLuPVIz9wMsoSsRMnJPlz46m41U4UMwcoHHcR8xruarpniL-GW94Z8Gj_al9KtnQA-jnHYGvGQvmzP9ss7A1Y-yiUaz2e2bK0DPPJubvYOWqNxLa2ZJghBWDT8sasx_DB6MJ5G-01HRFngnLEDWygN1vcy5MYzUYjg" alt=""></div>
<div class="av">+4</div>
</div>
</div>
<div class="card-lg-footer">
<div>
<span class="sparkline-label">Commit Velocity</span>
<div class="sparkline"><svg viewBox="0 0 100 20" preserveAspectRatio="none"><path d="M0 15 Q 10 5, 20 18 T 40 10 T 60 15 T 80 5 T 100 12" fill="none" stroke="#4f46e5" stroke-width="2" vector-effect="non-scaling-stroke"></path></svg></div>
</div>
<div class="card-stat">
<div><span class="card-stat-num">1,248</span><span class="card-stat-label">COMMITS</span></div>
<div><span class="card-stat-num">2m ago</span><span class="card-stat-label">LAST ACTIVE</span></div>
<button class="nav-icon"><span class="m material-symbols-outlined">more_vert</span></button>
</div>
</div>
</div>
<div class="card-sm">
<div class="card-sm-head"><h3>DataViz Engine</h3><span class="tag">v2.1.4</span></div>
<div class="card-sm-row"><span>Contributors</span><span>8 Active</span></div>
<div class="card-sm-sparkline"><svg viewBox="0 0 100 20" preserveAspectRatio="none"><path d="M0 18 L 10 12 L 20 15 L 30 5 L 40 10 L 50 18 L 60 8 L 70 12 L 80 5 L 90 10 L 100 15" fill="none" stroke="#89ceff" stroke-width="1.5" vector-effect="non-scaling-stroke"></path></svg></div>
<div class="card-sm-footer"><span>Last commit by <span class="hl" style="color:#c3c0ff">alex_m</span></span><span>1h ago</span></div>
</div>
<div class="card-sm">
<div class="card-sm-head"><h3>Auth-Middleware</h3><span class="m material-symbols-outlined" style="font-size:18px;color:#ffb4ab">warning</span></div>
<div class="card-sm-row"><span>Open Issues</span><span style="color:#ffb4ab">12 Critical</span></div>
<div class="card-sm-sparkline" style="opacity:.5"><svg viewBox="0 0 100 20" preserveAspectRatio="none"><path d="M0 10 L 20 10 L 40 10 L 60 10 L 80 10 L 100 10" fill="none" stroke="#918fa1" stroke-dasharray="2,2" stroke-width="1" vector-effect="non-scaling-stroke"></path></svg></div>
<div class="card-sm-footer"><span>Branch: <span class="hl">hotfix/vulnerabilities</span></span><span>Stale</span></div>
</div>
<div class="card-sm">
<div class="card-sm-head"><h3>Internal-CLI</h3><span class="m material-symbols-outlined" style="font-size:18px;color:#c3c0ff">verified</span></div>
<div class="card-sm-row"><span>Test Coverage</span><span style="color:#4ade80">98%</span></div>
<div class="card-sm-sparkline"><svg viewBox="0 0 100 20" preserveAspectRatio="none"><path d="M0 10 L 15 5 L 30 18 L 45 8 L 60 12 L 75 5 L 90 10 L 100 8" fill="none" stroke="#c3c0ff" stroke-width="1.5" vector-effect="non-scaling-stroke"></path></svg></div>
<div class="card-sm-footer"><span>Latest release: <span class="hl">v3.0.0-stable</span></span><span>Yesterday</span></div>
</div>
<div class="card-empty"><span class="m material-symbols-outlined">add_circle</span><span>Add project repository</span></div>
</div>
</div>

<div class="grid-4" style="display:flex;flex-direction:column;gap:24px">
<div class="sidebar-panel">
<div class="sidebar-panel-head"><h3>Recent Activity</h3><span class="m material-symbols-outlined">history</span></div>
<div class="sidebar-panel-body">
<div class="activity-item"><div class="activity-icon primary"><span class="m material-symbols-outlined">commit</span></div><div><div class="activity-text"><span class="hl">sarah_dev</span> pushed 3 commits to <span class="link">main</span></div><div class="activity-meta">12:45 PM &bull; BUILD-TOGETHER-UI</div></div></div>
<div class="activity-item"><div class="activity-icon tertiary"><span class="m material-symbols-outlined">merge</span></div><div><div class="activity-text"><span class="hl">james.wu</span> merged PR #452</div><div class="activity-meta">11:20 AM &bull; DATAVIZ-ENGINE</div></div></div>
<div class="activity-item"><div class="activity-icon error"><span class="m material-symbols-outlined">bug_report</span></div><div><div class="activity-text"><span class="hl">security_bot</span> flagged 2 vulnerabilities</div><div class="activity-meta">09:15 AM &bull; AUTH-MIDDLEWARE</div></div></div>
<div class="activity-item"><div class="activity-icon secondary"><span class="m material-symbols-outlined">comment</span></div><div><div class="activity-text"><span class="hl">emily_ux</span> commented on design specs</div><div class="activity-meta">08:30 AM &bull; BUILD-TOGETHER-UI</div></div></div>
</div>
<button class="view-all-btn">View All Activity</button>
</div>
<div class="sidebar-panel">
<div class="sidebar-panel-head"><h3>Upcoming Deployments</h3><span class="m material-symbols-outlined">rocket_launch</span></div>
<div class="sidebar-panel-body">
<div class="deploy-card">
<div class="deploy-bar primary"></div>
<div class="deploy-head"><span class="label primary">STAGING</span><span class="time">IN 25 MIN</span></div>
<p>BuildTogether UI Kit v4.0-rc1</p>
<div class="status-row"><span class="m material-symbols-outlined">check_circle</span><span>Tests passed</span></div>
</div>
<div class="deploy-card" style="opacity:.8">
<div class="deploy-bar tertiary"></div>
<div class="deploy-head"><span class="label tertiary">PRODUCTION</span><span class="time">TOMORROW</span></div>
<p>DataViz Engine Stable Release</p>
<div class="status-row"><span class="m material-symbols-outlined">info</span><span>Pending manual approval</span></div>
</div>
</div>
</div>
<div class="sidebar-panel">
<div class="sidebar-panel-head"><h3>Collaborator Activity</h3><span class="m material-symbols-outlined">analytics</span></div>
<div class="sidebar-panel-body">
<div class="perf-bar"><div class="perf-bar-head"><span class="name">Alex M.</span><span style="color:#c3c0ff;font-weight:700">428 LOC</span></div><div class="perf-bar-track"><div class="perf-bar-fill primary" style="width:85%"></div></div></div>
<div class="perf-bar"><div class="perf-bar-head"><span class="name">Sam R.</span><span style="color:#89ceff;font-weight:700">12 Commits</span></div><div class="perf-bar-track"><div class="perf-bar-fill secondary" style="width:60%"></div></div></div>
<div class="perf-bar"><div class="perf-bar-head"><span class="name">Jordan K.</span><span style="color:#ffb695;font-weight:700">8 Tasks</span></div><div class="perf-bar-track"><div class="perf-bar-fill tertiary" style="width:45%"></div></div></div>
</div>
<div class="total-velocity">
<div class="change">
<div><span class="label">TOTAL VELOCITY</span><span class="val">2.4k pts</span></div>
<div class="right"><span class="pct">+12%</span><span class="sub">VS LAST WEEK</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</main>
</div>

<footer class="footer-bar">
<span>&copy; 2024 BuildTogether. Technical Precision.</span>
<div class="footer-links">
<a href="#">Privacy</a><a href="#">Terms</a><a href="#">Documentation</a><a href="#">API</a>
<div class="status"><div class="dot"></div><span style="font-size:11px;font-weight:600;color:#c7c4d8;letter-spacing:.05em;font-family:'JetBrains Mono',monospace">Status</span></div>
</div>
</footer>
</div>
</body></html>"""

# Write all files
pages = {
    "landing.html": LANDING,
    "team.html": TEAM,
    "index.html": IDE,
    "dashboard.html": DASHBOARD,
}
for name, html in pages.items():
    (DIR / name).write_text(html, encoding="utf-8")
    print(f"  {name} ({len(html)} bytes)")
print(f"Done: {len(pages)} files")
