async function submitData() {
    const jsonInput = document.getElementById('jsonInput').value;
    const responseDiv = document.getElementById('response');
    const filters = document.querySelectorAll('#filters input[type="checkbox"]');

    try {
        const sanitizedInput = jsonInput.replace(/[“”]/g, '"');
        const jsonData = JSON.parse(sanitizedInput);
        const response = await fetch('/bfhl', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        });

        const data = await response.json();

        let filteredData = {};

        // If no filters selected, return the full response
        if ([...filters].every(filter => !filter.checked)) {
            filteredData = data;
        } else {
            // Otherwise, only include selected filters
            filters.forEach(filter => {
                if (filter.checked) {
                    filteredData[filter.value] = data[filter.value];
                }
            });
        }

        responseDiv.textContent = JSON.stringify(filteredData, null, 2);
    } catch (error) {
        responseDiv.textContent = 'Invalid JSON input';
    }
}
