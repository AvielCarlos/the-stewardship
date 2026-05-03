/* Live proposals view — pulls from GitHub Issues API.
 * Unauthenticated. 60 req/hr/IP. Reads only.
 */
(function () {
  const REPO = 'AvielCarlos/the-stewardship';
  const API = 'https://api.github.com/repos/' + REPO + '/issues?state=open&per_page=50';
  const status = document.getElementById('proposals-status');
  const list = document.getElementById('proposals-list');

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function fmtDate(iso) {
    try {
      const d = new Date(iso);
      return d.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' });
    } catch (_) {
      return iso;
    }
  }

  function labelChip(label) {
    const name = label.name || '';
    let cls = 'chip';
    if (name.startsWith('cp:')) cls = 'chip chip--cp';
    else if (name.startsWith('category:')) cls = 'chip chip--cat';
    else if (name.startsWith('state:')) cls = 'chip chip--state';
    else if (name === 'good-first-issue') cls = 'chip chip--first';
    else if (name === 'evolution') cls = 'chip chip--evo';
    else if (name === 'infrastructure') cls = 'chip chip--infra';
    else if (name === 'proposal') cls = 'chip chip--proposal';
    return '<span class="' + cls + '">' + escapeHtml(name) + '</span>';
  }

  function renderItem(it) {
    const isPullRequest = !!it.pull_request;
    if (isPullRequest) return '';
    const reactions = it.reactions || {};
    const positive =
      (reactions['+1'] || 0) + (reactions['heart'] || 0) + (reactions['rocket'] || 0) + (reactions['hooray'] || 0);
    const concerns = (reactions['-1'] || 0) + (reactions['confused'] || 0);
    const labels = (it.labels || []).map(labelChip).join('');
    return (
      '<article class="proposal">' +
      '<div class="proposal__head">' +
      '<a class="proposal__title" href="' +
      escapeHtml(it.html_url) +
      '" target="_blank" rel="noopener">#' +
      it.number +
      ' · ' +
      escapeHtml(it.title) +
      '</a>' +
      '<div class="proposal__meta">' +
      '<span>opened ' +
      fmtDate(it.created_at) +
      '</span>' +
      (it.user && it.user.login
        ? '<span>by <a href="' + escapeHtml(it.user.html_url) + '" target="_blank" rel="noopener">' + escapeHtml(it.user.login) + '</a></span>'
        : '') +
      '<span>💬 ' +
      (it.comments || 0) +
      '</span>' +
      '<span class="signal signal--pos">↑ ' +
      positive +
      '</span>' +
      '<span class="signal signal--neg">↓ ' +
      concerns +
      '</span>' +
      '</div>' +
      '</div>' +
      (labels ? '<div class="proposal__labels">' + labels + '</div>' : '') +
      '<div class="proposal__actions">' +
      '<a class="btn-ghost btn-ghost--sm" href="' +
      escapeHtml(it.html_url) +
      '" target="_blank" rel="noopener">Read & react ↗</a>' +
      '</div>' +
      '</article>'
    );
  }

  fetch(API, { headers: { Accept: 'application/vnd.github+json' } })
    .then(function (r) {
      if (!r.ok) throw new Error('GitHub API ' + r.status);
      return r.json();
    })
    .then(function (issues) {
      const items = issues.filter(function (i) {
        return !i.pull_request;
      });
      if (!items.length) {
        status.textContent = 'No open proposals or tasks yet. Be the first.';
        return;
      }
      status.textContent = items.length + ' open · sorted by newest';
      // newest first
      items.sort(function (a, b) {
        return new Date(b.created_at) - new Date(a.created_at);
      });
      list.innerHTML = items.map(renderItem).join('');
    })
    .catch(function (err) {
      status.textContent = 'Could not load from GitHub (' + (err && err.message ? err.message : 'error') + '). View on GitHub directly →';
      list.innerHTML =
        '<a class="btn-primary" href="https://github.com/AvielCarlos/the-stewardship/issues">Open in GitHub</a>';
    });
})();
