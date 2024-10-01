document.addEventListener('DOMContentLoaded', () => {
    const cardContainer = document.getElementById('card-container');

    // Function to render cards dynamically
    function renderCards(cards) {
        cards.forEach((card, index) => {
            const cardElement = document.createElement('div');
            cardElement.className = 'card'; 
            cardElement.setAttribute('draggable', true); 

            cardElement.innerHTML = `
                <div class="brown-field">
                    <img src="${card.image_url}" alt="${card.name}" class="card-image">
                    <div class="dropdown" style="display: none;">
                        <ul>
                            <li>Tap</li>
                            <li>Return</li>
                            <li>Activate ability</li>
                        </ul>
                    </div>
                </div>
            `;

            // Double-click to flip/rotate the card
            cardElement.addEventListener('dblclick', (e) => {
                e.preventDefault(); // Prevent the default behavior
                cardElement.classList.toggle('rotate'); // Toggle the rotation
            });

            // Drag events
            cardElement.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', index); // Use the index for transfer
                e.dataTransfer.effectAllowed = 'move'; // Indicate that we're moving
                cardElement.style.opacity = '0.5'; // Change opacity while dragging
            });

            cardElement.addEventListener('dragend', () => {
                cardElement.style.opacity = '1'; // Reset opacity
            });

            // Hover event for dropdown
            const brownField = cardElement.querySelector('.brown-field');
            const dropdown = cardElement.querySelector('.dropdown');
            let hoverTimeout;

            brownField.addEventListener('mouseenter', () => {
                hoverTimeout = setTimeout(() => {
                    dropdown.style.display = 'block'; // Show dropdown after 1 second
                }, 1000); // 1 second delay
            });

            brownField.addEventListener('mouseleave', () => {
                clearTimeout(hoverTimeout); // Cancel the timer if user leaves early
                dropdown.style.display = 'none'; // Hide dropdown
            });

            cardContainer.appendChild(cardElement);
        });
    }

    const cardData = {{ cards | tojson }};
    renderCards(cardData);

    // Handle dragover and drop events
    cardContainer.addEventListener('dragover', (e) => {
        e.preventDefault(); // Prevent default to allow drop
        e.dataTransfer.dropEffect = 'move'; // Show move effect
    });

    cardContainer.addEventListener('drop', (e) => {
        e.preventDefault(); // Prevent default action
        const index = e.dataTransfer.getData('text/plain'); // Get the index of the dragged card
        const draggedCard = cardContainer.children[index]; // Get the card element

        // Calculate mouse position for new placement
        const rect = cardContainer.getBoundingClientRect();
        const offsetX = e.clientX - rect.left;
        const offsetY = e.clientY - rect.top;

        // Position the card based on mouse position
        draggedCard.style.position = 'absolute'; // Ensure it is positioned absolutely
        draggedCard.style.left = `${offsetX - draggedCard.offsetWidth / 2}px`;
        draggedCard.style.top = `${offsetY - draggedCard.offsetHeight / 2}px`;

        // Remove the card from the container and re-add it to create the new position
        cardContainer.removeChild(draggedCard);
        cardContainer.appendChild(draggedCard);
    });
});