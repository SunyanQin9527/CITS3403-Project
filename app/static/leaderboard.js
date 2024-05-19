// Leaderboard.js

// Updates the leaderboard with the given data
document.addEventListener('DOMContentLoaded', function() {
    const leaderboardData = [
        { name: 'Alice Johnson', score: 1200 },
        { name: 'Bob Smith', score: 1100 },
        { name: 'Carol Tan', score: 1050 },
        // Add more users as needed
        { name: 'Dave Lee', score: 1040 },
        { name: 'Eva Green', score: 1030 },
        { name: 'Frank Moore', score: 1020 },
        { name: 'Gina Hall', score: 1010 },
        { name: 'Henry Dale', score: 1005 },
        { name: 'Ivy Poe', score: 1000 },
        { name: 'Jack Neil', score: 995 }
    ];

    function updateLeaderboard(data) {
        const leaderboardList = document.getElementById('leaderboardList');
        leaderboardList.innerHTML = ''; // Clear current list

        // Generate rankings for the top 10
        const placements = ['1st Place', '2nd Place', '3rd Place', '4th Place', '5th Place',
                            '6th Place', '7th Place', '8th Place', '9th Place', '10th Place'];

        data.slice(0, 10).forEach((user, index) => {
            const listItem = document.createElement('li');
            listItem.className = `leaderboard-entry ${placements[index].toLowerCase().replace(' ', '-')}`;
            listItem.innerHTML = `
                <span class="placement">${placements[index]} - </span>
                <span class="user-name">${user.name}</span> - 
                <span class="user-score">${user.score}</span> points
            `;
            leaderboardList.appendChild(listItem);
        });
    }

    updateLeaderboard(leaderboardData);
});

