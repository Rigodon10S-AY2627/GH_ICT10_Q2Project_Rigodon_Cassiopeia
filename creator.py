
from pyscript import document

creator_name = "Cassiopeia Rigodon"

interests = [
    "Animals",
    "Academic competitions",
    "Pop Mart figurines",
    "Building friendships and meeting new people"
]

hobbies = [
    "Talking with friends",
    "Watching C-dramas, K-dramas, and J-dramas",
    "Playing online games",
    "Scrolling through social media",
    "Participating in academic competitions"
]

dreams = [
    "To travel around the world",
    "To buy the things I couldn't afford as a minor",
    "To finally be free from school",
    "To become the best version of myself, like the version of me in a parallel world called Best Versions"
]

document.getElementById("creator-content").innerHTML = f"""
<div class="creator-profile">
    <h2>{creator_name}</h2>
    <p class="creator-subtitle">Grade 10 Student</p>

    <h3>My Interests</h3>
    <ul>
        {''.join(f'<li>{item}</li>' for item in interests)}
    </ul>

    <h3>My Hobbies</h3>
    <ul>
        {''.join(f'<li>{item}</li>' for item in hobbies)}
    </ul>

    <h3>My Dreams and Aspirations</h3>
    <ul>
        {''.join(f'<li>{item}</li>' for item in dreams)}
    </ul>
</div>
"""
