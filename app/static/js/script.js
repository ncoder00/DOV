document.getElementById('analyze-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const userInput = e.target.user_input.value;
    showLoading();
    fetchResults(userInput);
});

function showLoading() {
    const loading = document.getElementById('loading');
    loading.style.display = 'block';
}

function hideLoading() {
    const loading = document.getElementById('loading');
    loading.style.display = 'none';
}

function fetchResults(input) {
    fetch(`/results/${input}`)
        .then(response => response.json())
        .then(data => {
            displayResults(data);
            hideLoading();
        })
        .catch(error => {
            console.error('Error:', error);
            hideLoading();
        });
}

function displayResults(data) {
    const container = document.getElementById('results-container');
    container.innerHTML = ''; // Clear previous results

    const expandCollapseAllButton = document.getElementById('expand-collapse-all');
    expandCollapseAllButton.style.display = 'block'; // Show the expand/collapse button

    if (data.whois_results) {
        container.appendChild(createResultCard('WHOIS Lookup', data.whois_results));
    }
    if (data.dns_results) {
        container.appendChild(createResultCard('DNS Lookup', data.dns_results));
    }
    if (data.ssl_results) {
        container.appendChild(createResultCard('SSL Certificate', data.ssl_results));
    }
    if (data.http_header_results) {
        container.appendChild(createResultCard('HTTP Headers', data.http_header_results));
    }
    if (data.geolocation_results) {
        container.appendChild(createResultCard('Geolocation', data.geolocation_results));
    }
}

function createResultCard(title, results) {
    const card = document.createElement('div');
    card.classList.add('result-card', 'collapsed');
    card.onclick = () => toggleCard(card);

    const cardTitle = document.createElement('h2');
    cardTitle.textContent = title;
    card.appendChild(cardTitle);

    const content = document.createElement('div');
    content.classList.add('card-content');
    content.style.display = 'none';

    if (results.Error) {
        const error = document.createElement('p');
        error.textContent = `Error: ${results.Error}`;
        content.appendChild(error);
    } else {
        const table = document.createElement('table');
        const tbody = document.createElement('tbody');
        Object.entries(results).forEach(([key, value]) => {
            const tr = document.createElement('tr');
            const tdKey = document.createElement('td');
            const tdValue = document.createElement('td');
            tdKey.textContent = key;
            tdValue.textContent = Array.isArray(value) ? value.join(', ') : value;
            tr.appendChild(tdKey);
            tr.appendChild(tdValue);
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        content.appendChild(table);
    }

    card.appendChild(content);
    return card;
}

function toggleCard(card) {
    const content = card.querySelector('.card-content');
    if (card.classList.contains('collapsed')) {
        card.classList.remove('collapsed');
        card.classList.add('expanded');
        content.style.display = 'block';
    } else {
        card.classList.remove('expanded');
        card.classList.add('collapsed');
        content.style.display = 'none';
    }
}

function toggleAllCards() {
    const cards = document.querySelectorAll('.result-card');
    const allExpanded = Array.from(cards).every(card => card.classList.contains('expanded'));
    cards.forEach(card => {
        const content = card.querySelector('.card-content');
        if (allExpanded) {
            card.classList.remove('expanded');
            card.classList.add('collapsed');
            content.style.display = 'none';
        } else {
            card.classList.remove('collapsed');
            card.classList.add('expanded');
            content.style.display = 'block';
        }
    });

    const button = document.getElementById('expand-collapse-all');
    button.textContent = allExpanded ? '+' : '-';
}
