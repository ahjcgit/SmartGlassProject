'use strict';
// Filtering changes only which measured trials are visible; never the values.
const filters = document.querySelectorAll('[data-filter]');
const rows = document.querySelectorAll('tbody tr[data-object]');
for (const button of filters) button.addEventListener('click', () => {
  const selected = button.dataset.filter;
  for (const filter of filters) filter.setAttribute('aria-pressed', String(filter === button));
  let count = 0;
  for (const row of rows) { row.hidden = selected !== 'all' && row.dataset.object !== selected; if (!row.hidden) count++; }
  document.getElementById('filter-status').textContent = `Showing ${selected === 'all' ? 'all ' : ''}${count} ${count === 1 ? 'trial' : 'trials'}${selected === 'all' ? '.' : ' · ' + button.textContent + '.'}`;
});
