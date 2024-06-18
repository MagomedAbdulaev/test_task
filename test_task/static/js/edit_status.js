const edit_buttons = document.querySelectorAll('.table-clients .client .edit--button');
const menu_statuses = document.querySelectorAll('.table-clients .client .menu__statuses');

for (let btn = 0; btn < edit_buttons.length; btn++) {
    edit_buttons[btn].addEventListener('click', (event) => {
        event.stopPropagation(); // Остановка всплытия события
        menu_statuses[btn].classList.toggle('menu--active');
        if (menu_statuses[btn].classList.contains('menu--active')) {
            let list_buttons = menu_statuses[btn].querySelectorAll('.menu__item');
            for (let item of list_buttons) {
                item.addEventListener('click', (event) => {
                    event.stopPropagation(); // Остановка всплытия события
                    let item_obj = {
                        'client_id': item.dataset.setId,
                        'type': item.dataset.setType,
                    };
                    fetch('/client_status_fetch/', {
                        method: 'POST',
                        headers: { 'X-CSRFToken': csrf_token },
                        mode: 'same-origin',
                        body: JSON.stringify(item_obj),
                    })
                    .then(response => response.json())
                    .then(result => {
                        const status_value = document.querySelectorAll('.table-clients .client .client__item .status_value')[btn];
                        status_value.innerHTML = item.textContent;
                        menu_statuses[btn].classList.remove('menu--active');
                    });
                });
            }
        }
    });
}

// Закрытие модалки при клике вне её
document.addEventListener('click', (event) => {
    for (let btn = 0; btn < menu_statuses.length; btn++) {
        if (menu_statuses[btn].classList.contains('menu--active') && !menu_statuses[btn].contains(event.target) && !edit_buttons[btn].contains(event.target)) {
            menu_statuses[btn].classList.remove('menu--active');
        }
    }
});