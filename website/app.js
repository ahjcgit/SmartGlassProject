'use strict';
const filter = document.getElementById('object-filter');
const rows = document.querySelectorAll('.trial-table tbody tr[data-object]');
filter.addEventListener('change', () => {
  let count = 0;
  for (const row of rows) {
    row.hidden = filter.value !== 'all' && row.dataset.object !== filter.value;
    if (!row.hidden) count++;
  }
  document.getElementById('filter-status').textContent =
    `Showing ${count} ${count === 1 ? 'trial' : 'trials'} for ${filter.selectedOptions[0].textContent.toLowerCase()}.`;
});
