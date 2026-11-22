
from pyscript import document

_name = "Cassiopeia Rigodon"
age = 15
height1 = 157.48
countries_visit = ["Germany", "France", "United Kingdom"]
student_type = False
student_info = {
    "color": "Lavender",
    "car_brand": "BYD",
    "shoe_size": 8,
    "best_friend": "Elijah Mae"
}
favorite_fruits = {"Lychee", "Kiwi", "Rambutan", "Mango", "Melon"}
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

countries = ", ".join(countries_visit)
fruits = ", ".join(sorted(favorite_fruits))
weekdays = ", ".join(days)

document.getElementById("profile-content").innerHTML = f'''
    <div class="profile-grid">
        <div class="profile-main">
            <div class="profile-topline">
                <span class="profile-tag">PERSONAL PROFILE</span>
                <span class="profile-status">● STUDENT PROFILE</span>
            </div>
            <div class="profile-avatar">CR</div>
            <p class="profile-small">HELLO, I'M</p>
            <h3>{_name}</h3>
            <p class="profile-description">A student who enjoys learning, exploring new interests, and taking on different challenges.</p>
            <div class="profile-details">
                <div><span>Age</span><strong>{age}</strong></div>
                <div><span>Height</span><strong>{height1} cm</strong></div>
                <div><span>Student type</span><strong>{student_type}</strong></div>
            </div>
        </div>
        <div class="profile-side">
            <div class="data-card">
                <span class="data-label">01 / COUNTRIES VISITED</span>
                <h4>Places I've been</h4>
                <p>{countries}</p>
            </div>
            <div class="data-card">
                <span class="data-label">02 / FAVORITE FRUITS</span>
                <h4>Fruit favorites</h4>
                <p>{fruits}</p>
            </div>
            <div class="data-card">
                <span class="data-label">03 / PERSONAL DETAILS</span>
                <h4>A few more things</h4>
                <p><strong>Favorite color:</strong> {student_info["color"]}</p>
                <p><strong>Car brand:</strong> {student_info["car_brand"]}</p>
                <p><strong>Shoe size:</strong> {student_info["shoe_size"]}</p>
                <p><strong>Best friend:</strong> {student_info["best_friend"]}</p>
            </div>
        </div>
    </div>
    <div class="data-types-section">
        <div class="data-types-heading">
            <div>
                <span class="data-label">PYTHON / SEATWORK 1</span>
                <h3>Data types in action.</h3>
            </div>
            <p>The information above demonstrates different Python data types.</p>
        </div>
        <div class="type-grid">
            <div class="type-item"><span>STRING</span><strong>{_name}</strong><small>Text value</small></div>
            <div class="type-item"><span>INTEGER</span><strong>{age}</strong><small>Whole number</small></div>
            <div class="type-item"><span>FLOAT</span><strong>{height1}</strong><small>Decimal number</small></div>
            <div class="type-item"><span>BOOLEAN</span><strong>{student_type}</strong><small>True or False</small></div>
            <div class="type-item"><span>LIST</span><strong>{len(countries_visit)} items</strong><small>Countries visited</small></div>
            <div class="type-item"><span>DICTIONARY</span><strong>{len(student_info)} pairs</strong><small>Personal details</small></div>
            <div class="type-item"><span>SET</span><strong>{len(favorite_fruits)} items</strong><small>Favorite fruits</small></div>
            <div class="type-item"><span>TUPLE</span><strong>{len(days)} items</strong><small>Days of the week</small></div>
        </div>
        <div class="days-note">
            <span>THE DAYS OF THE WEEK</span>
            <p>{weekdays}</p>
        </div>
    </div>
'''
