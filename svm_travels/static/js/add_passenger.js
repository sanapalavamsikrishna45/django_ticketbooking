document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ticket-form');
    const select = document.getElementById('passenger-select');
    const addBtn = document.getElementById('add-passenger-btn');

    const passengerListUrl = form.dataset.passengerListUrl;
    const passengerAddUrl = form.dataset.passengerAddUrl;

    // Fetch existing passengers
    fetch(passengerListUrl)
        .then(res => res.json())
        .then(data => {
            data.forEach(p => {
                const option = document.createElement('option');
                option.value = p.id;
                option.textContent = `${p.name} (${p.age}, ${p.gender})`;
                select.appendChild(option);
            });
        });

    // Add new passenger via API
    addBtn.addEventListener('click', function() {
        const name = document.getElementById('new-name').value.trim();
        const age = document.getElementById('new-age').value;
        const gender = document.getElementById('new-gender').value;

        if (!name || !age || !gender) {
            alert('Please fill all fields.');
            return;
        }

        fetch(passengerAddUrl, {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ name, age, gender })
        })
        .then(res => res.json())
        .then(p => {
            const option = document.createElement('option');
            option.value = p.id;
            option.textContent = `${p.name} (${p.age}, ${p.gender})`;
            option.selected = true;
            select.appendChild(option);

            document.getElementById('new-name').value = '';
            document.getElementById('new-age').value = '';
            document.getElementById('new-gender').value = '';
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
