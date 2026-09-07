/* The complete article list is in HTML; filtering is a progressive enhancement. */
(() => {
  const search = document.querySelector('#search');
  if (!search) return;
  const posts = [...document.querySelectorAll('.post')];
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const count = document.querySelector('#result-count');
  let category = '全部';
  function filter() {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    posts.forEach(post => {
      const match = (category === '全部' || post.dataset.category === category) && post.textContent.toLocaleLowerCase().includes(query);
      post.hidden = !match;
      if (match) visible++;
    });
    count.textContent = `${visible} 篇文章`;
    document.querySelector('#empty').hidden = visible !== 0;
  }
  buttons.forEach(button => button.addEventListener('click', () => {
    category = button.dataset.filter;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    filter();
  }));
  search.addEventListener('input', filter);
  document.querySelector('.filters').hidden = false;
  document.querySelector('.search-box').hidden = false;
})();
