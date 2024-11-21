document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.getElementById('add_item');
  const ul = document.querySelector('ul.my_list');

  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
  });
});
