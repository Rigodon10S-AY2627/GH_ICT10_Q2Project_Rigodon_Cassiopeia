
# PA2 - Working with Sets
from pyscript import document

# Predefined Grade 7 members
grade_7 = {"Victoria Rivera", "Reuben Lim", "Antonio Manalo"}

# Predefined Grade 8 members
grade_8 = {"Elaina Daclan", "Kristine Manabat", "Arkin Cuenca"}

# Predefined Grade 9 members
grade_9 = {"Cedric Visorde", "Dan Perez", "Na Yeon Kim"}

# Predefined Grade 10 members
grade_10 = {"Lara Estrada", "Cassiopeia Rigodon", "Zangief Briones"}

# Combine all grade sets using union
ict_members = grade_7 | grade_8 | grade_9 | grade_10

# Display the initial member count and list
document.getElementById("results").innerHTML = (
    f"<h3>Total Members: {len(ict_members)}</h3>"
    f"<p>{', '.join(sorted(ict_members))}</p>"
)

# Add a new member
def add_member(e):
    first_name = document.getElementById("first-name").value
    last_name = document.getElementById("last-name").value

    full_name = f"{first_name.strip().title()} {last_name.strip().title()}"

    # Add the new member using set union
    new_member = {full_name}
    ict_members.update(new_member)

    # Display the updated total and member list
    document.getElementById("results").innerHTML = (
        f"<h3>Total Members: {len(ict_members)}</h3>"
        f"<p>{', '.join(sorted(ict_members))}</p>"
    )

    # Clear the input fields
    document.getElementById("first-name").value = ""
    document.getElementById("last-name").value = ""
