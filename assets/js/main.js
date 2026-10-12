/* ==========================================================================
   Kavitha Digital — main.js — V1
   Vanilla JavaScript, no libraries. Loaded with `defer` on every page.

   Everything here is progressive enhancement: with JavaScript switched off,
   every page is still fully readable, the menu is shown as a list, FAQs open
   natively (<details>) and the contact form still reaches WhatsApp.
   Each feature runs inside safe() so one failure never breaks the others.

    1. Sticky header state, back-to-top and phone contact-bar visibility
    2. Mobile menu (focus-trapped, Escape to close)
    3. Dropdown / mega menus (click, keyboard, hover-intent)
    4. Scroll-reveal animations (IntersectionObserver)
    5. Number counters
    6. Back-to-top button
    7. Footer year
    8. Contact form (form service endpoint OR WhatsApp hand-off)
    9. Blog category filter
   ========================================================================== */
(function () {
  'use strict';

  var doc = document;
  var root = doc.documentElement;
  var body = doc.body;
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var desktopMQ = window.matchMedia ? window.matchMedia('(min-width: 1181px)') : { matches: true, addEventListener: function () {} };

  function $(sel, ctx) { return (ctx || doc).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }
  function safe(fn) { try { fn(); } catch (err) { if (window.console) console.warn('[Kavitha Digital]', err); } }
  function onMQChange(mq, fn) {
    if (mq.addEventListener) mq.addEventListener('change', fn);
    else if (mq.addListener) mq.addListener(fn);
  }


  /* ---------- 1. Sticky header, back-to-top and contact-bar visibility ---------- */
  safe(function () {
    var header = $('.site-header');
    var toTop = $('.to-top');
    var fabs = $('.fab-stack');
    if (!header && !toTop) return;
    var ticking = false;
    var lastY = window.pageYOffset || 0;

    function update() {
      var y = window.pageYOffset || root.scrollTop;
      if (header) header.classList.toggle('is-scrolled', y > 8);
      if (toTop) toTop.classList.toggle('is-visible', y > 700);
      // Phone contact bar slides away while reading down, returns when scrolling up
      // (hiding only takes effect below 640px — see responsive.css)
      if (fabs && Math.abs(y - lastY) > 6) {
        fabs.classList.toggle('is-hidden', y > lastY && y > 320);
        lastY = y;
      }
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(update); }
    }, { passive: true });
    update();
  });


  /* ---------- 2. Mobile menu ---------- */
  safe(function () {
    var toggle = $('.nav-toggle');
    var nav = $('#site-nav');
    if (!toggle || !nav) return;
    var label = $('.nav-toggle__text', toggle);

    function isOpen() { return nav.classList.contains('is-open'); }

    function setOpen(open, returnFocus) {
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      if (label) label.textContent = open ? 'Close' : 'Menu';
      body.classList.toggle('nav-open', open);
      if (open) {
        var first = $('a, button', nav);
        if (first) first.focus({ preventScroll: true });
      } else if (returnFocus) {
        toggle.focus();
      }
    }

    toggle.addEventListener('click', function () { setOpen(!isOpen(), false); });

    doc.addEventListener('keydown', function (e) {
      if (!isOpen() || desktopMQ.matches) return;
      if (e.key === 'Escape') { setOpen(false, true); return; }
      if (e.key !== 'Tab') return;
      // Keep keyboard focus inside the open menu
      var focusables = [toggle].concat($$('a[href], button:not([disabled])', nav).filter(function (el) {
        return el.offsetParent !== null;
      }));
      var first = focusables[0];
      var last = focusables[focusables.length - 1];
      if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    // Following a link closes the panel (matters for same-page anchors)
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && !desktopMQ.matches) setOpen(false, false);
    });

    // Reset when the viewport grows into desktop layout
    onMQChange(desktopMQ, function (e) { if (e.matches && isOpen()) setOpen(false, false); });
  });


  /* ---------- 3. Dropdown / mega menus ---------- */
  safe(function () {
    var items = $$('.nav-item.has-sub');
    if (!items.length) return;

    function setItem(item, open) {
      item.classList.toggle('is-open', open);
      var btn = $('.sub-toggle', item);
      if (btn) btn.setAttribute('aria-expanded', String(open));
    }
    function closeAll(except) {
      items.forEach(function (item) { if (item !== except && item.classList.contains('is-open')) setItem(item, false); });
    }

    items.forEach(function (item) {
      var btn = $('.sub-toggle', item);
      var leaveTimer;
      if (!btn) return;

      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var open = !item.classList.contains('is-open');
        if (desktopMQ.matches) closeAll(item);
        setItem(item, open);
        if (open && desktopMQ.matches) {
          var firstLink = $('.submenu a', item);
          if (firstLink && e.detail === 0) firstLink.focus(); // keyboard activation only
        }
      });

      // Desktop: close when keyboard focus leaves the item
      item.addEventListener('focusout', function (e) {
        if (desktopMQ.matches && !item.contains(e.relatedTarget)) setItem(item, false);
      });

      // Desktop hover-intent: a click-opened menu closes shortly after the pointer leaves
      item.addEventListener('mouseleave', function () {
        if (!desktopMQ.matches) return;
        leaveTimer = window.setTimeout(function () { setItem(item, false); }, 220);
      });
      item.addEventListener('mouseenter', function () { window.clearTimeout(leaveTimer); });
    });

    doc.addEventListener('click', function (e) {
      if (desktopMQ.matches && !e.target.closest('.nav-item.has-sub')) closeAll(null);
    });

    doc.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape' || !desktopMQ.matches) return;
      var open = $('.nav-item.has-sub.is-open');
      if (open) {
        setItem(open, false);
        var btn = $('.sub-toggle', open);
        if (btn) btn.focus();
      }
    });

    onMQChange(desktopMQ, function () { closeAll(null); });
  });


  /* ---------- 4. Scroll-reveal animations ---------- */
  safe(function () {
    var els = $$('[data-reveal]');
    if (!els.length || reduceMotion || !('IntersectionObserver' in window)) return;

    // Stagger children inside [data-reveal-stagger] groups
    $$('[data-reveal-stagger]').forEach(function (group) {
      $$('[data-reveal]', group).forEach(function (el, i) {
        el.style.setProperty('--delay', Math.min(i * 70, 420) + 'ms');
      });
    });

    // Anything already on screen stays visible — no flash, no LCP delay
    var vh = window.innerHeight || root.clientHeight;
    els.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < vh && r.bottom > 0) el.classList.add('is-visible');
    });
    root.classList.add('reveal-ready');

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });

    els.forEach(function (el) { if (!el.classList.contains('is-visible')) io.observe(el); });

    // Printing or saving as PDF shows everything
    window.addEventListener('beforeprint', function () {
      els.forEach(function (el) { el.classList.add('is-visible'); });
    });
  });


  /* ---------- 5. Number counters ---------- */
  safe(function () {
    var counters = $$('[data-count]');
    if (!counters.length || reduceMotion || !('IntersectionObserver' in window)) return;

    function run(el) {
      var target = parseFloat(el.getAttribute('data-count')) || 0;
      var suffix = el.getAttribute('data-suffix') || '';
      var duration = 1300;
      var start = null;
      function step(ts) {
        if (!start) start = ts;
        var p = Math.min((ts - start) / duration, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased) + suffix;
        if (p < 1) window.requestAnimationFrame(step);
      }
      window.requestAnimationFrame(step);
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        run(entry.target);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { io.observe(el); });
  });


  /* ---------- 6. Back-to-top button ---------- */
  safe(function () {
    var btn = $('.to-top');
    if (!btn) return;
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      var logo = $('.site-header .logo');
      if (logo) logo.focus({ preventScroll: true });
    });
  });


  /* ---------- 7. Footer year ---------- */
  safe(function () {
    var year = String(new Date().getFullYear());
    $$('[data-year]').forEach(function (el) { el.textContent = year; });
  });


  /* ---------- 8. Contact form ----------
     data-endpoint=""  → the enquiry is handed to WhatsApp (works on GitHub Pages today)
     data-endpoint="https://formspree.io/f/xxxx" (or Web3Forms / Netlify / your API)
                       → posted with fetch, success shown inline.
     Set the endpoint once in tools/site_config.py and rebuild. */
  safe(function () {
    var form = $('[data-contact-form]');
    if (!form) return;
    var status = $('.form-status', form);
    var endpoint = (form.getAttribute('data-endpoint') || '').trim();
    var waNumber = form.getAttribute('data-whatsapp') || '';
    var phoneText = form.getAttribute('data-phone') || '';
    var submitBtn = $('[type="submit"]', form);
    form.setAttribute('novalidate', '');

    function fieldOf(input) { return input.closest('.field') || input.closest('.checkbox'); }

    function check(input) {
      var wrap = fieldOf(input);
      var ok = input.checkValidity();
      if (wrap) wrap.classList.toggle('is-invalid', !ok);
      if (ok) input.removeAttribute('aria-invalid');
      else input.setAttribute('aria-invalid', 'true');
      return ok;
    }

    var inputs = $$('input:not([type="hidden"]):not([name="_gotcha"]), select, textarea', form);
    inputs.forEach(function (input) {
      input.addEventListener('blur', function () { if (input.value) check(input); });
      input.addEventListener('input', function () {
        var wrap = fieldOf(input);
        if (wrap && wrap.classList.contains('is-invalid')) check(input);
      });
    });

    function say(msg, state) {
      if (!status) return;
      status.textContent = msg;
      if (state) status.setAttribute('data-state', state); else status.removeAttribute('data-state');
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var firstBad = null;
      inputs.forEach(function (input) { if (!check(input) && !firstBad) firstBad = input; });
      if (firstBad) {
        say('Please check the highlighted fields.', 'error');
        firstBad.focus();
        return;
      }

      var data = new FormData(form);
      if (data.get('_gotcha')) return; // spam trap

      if (endpoint) {
        if (submitBtn) submitBtn.disabled = true;
        say('Sending…');
        fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (res) {
            if (!res.ok) throw new Error('Request failed');
            form.reset();
            say('Thank you — your enquiry has been sent. Harish will get back to you shortly.');
          })
          .catch(function () {
            say('Sorry, that did not go through. Please call or WhatsApp ' + phoneText + ' instead.', 'error');
          })
          .then(function () { if (submitBtn) submitBtn.disabled = false; });
        return;
      }

      // WhatsApp hand-off: builds a tidy message and opens WhatsApp ready to send
      var lines = [
        'Hi Harish, I have an enquiry from the Kavitha Digital website.',
        '',
        'Name: ' + (data.get('name') || ''),
        'Phone: ' + (data.get('phone') || '')
      ];
      if (data.get('email')) lines.push('Email: ' + data.get('email'));
      if (data.get('business')) lines.push('Business: ' + data.get('business'));
      if (data.get('service')) lines.push('Interested in: ' + data.get('service'));
      lines.push('', 'Message: ' + (data.get('message') || data.get('text') || ''));

      var url = 'https://wa.me/' + waNumber + '?text=' + encodeURIComponent(lines.join('\n'));
      // Note: window.open(..., 'noopener') always returns null, so opener is cleared manually
      var win = window.open(url, '_blank');
      if (win) { try { win.opener = null; } catch (err) { /* cross-origin */ } }
      else { window.location.href = url; } // pop-up blocked: continue in this tab
      say('WhatsApp has opened with your enquiry — tap Send to deliver it to Harish.');
    });
  });


  /* ---------- 9. Blog category filter ---------- */
  safe(function () {
    var bar = $('[data-filter-bar]');
    if (!bar) return;
    var cards = $$('[data-category]');
    var live = $('[data-filter-status]');
    bar.hidden = false; // only shown when JavaScript can make it work

    bar.addEventListener('click', function (e) {
      var btn = e.target.closest('button[data-filter]');
      if (!btn) return;
      var cat = btn.getAttribute('data-filter');
      $$('button[data-filter]', bar).forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      var shown = 0;
      cards.forEach(function (card) {
        var match = cat === 'all' || (' ' + card.getAttribute('data-category') + ' ').indexOf(' ' + cat + ' ') > -1;
        card.hidden = !match;
        if (match) shown++;
      });
      if (live) live.textContent = 'Showing ' + shown + (shown === 1 ? ' article' : ' articles');
    });
  });

})();
