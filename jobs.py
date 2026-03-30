from database import get_connection

def add_job():
    print("\nADD NEW JOB")
    title = input("Enter job title: ")
    required_skills = input("Enter required skills (separated by comma): ")

    # Ensuring that we don't get empty input for both fields (the title and the required skills).
    if not title or not required_skills:
        print("Title and required skills cannot be empty.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Insert the new job into the jobs table
        cursor.execute("INSERT INTO jobs (title, required_skills) VALUES (%s, %s)", (title, required_skills))
        conn.commit()
        print(f"\n{title} added successfully!")

    except Exception as e:
        # We're print the error anytime there's a thing that goes wrong instead of crashing the entire program.
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()

def view_jobs():
    print("\nALL AVAILABLE JOBS")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, title, required_skills FROM jobs")
        jobs = cursor.fetchall()

        if not jobs:
            print("No jobs found.")
        else:
            print("-" * 40)
            print(f"{'ID':<5} {'Title':<20} {'Required Skills'}")
            print("-" * 40)
            for job in jobs:
                print(f"{job[0]:<5} {job[1]:<20} {job[2]}")
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()

def update_job():
    print("UPDATE JOB")

    conn = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="skillmatch"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, skills FROM jobs")
    jobs = cursor.fetchall()

    if not jobs:
        conn.close()
        return

    print("available jobs:")
    for job in jobs:
        print(f"  ID: {job[0]} | TITLE: {job[1]} | SKILLS: {job[2]}")

    try:
        job_id = int(input("enter job ID to update: "))
    except ValueError:
        conn.close()
        return

    cursor.execute("SELECT id, title, skills FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()

    if not job:
        conn.close()
        return

    print(f"\nUPDATING JOB: {job[1]}")
    new_title = input(f" enter new title (leave blank to keep '{job[1]}'): ").strip()
    new_skills = input(f" enter new skills (leave blank to keep '{job[2]}'): ").strip()

    updated_title = new_title if new_title else job[1]
    updated_skills = new_skills if new_skills else job[2]

    cursor.execute(
        "UPDATE jobs SET title = %s, skills = %s WHERE id = %s",
        (updated_title, updated_skills, job_id)
    )
    conn.commit()
    conn.close()

def delete_job():
    print("\nDELETE JOB")
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Show all jobs so the person can pick which one to delete
        cursor.execute("SELECT id, title, required_skills FROM jobs")
        jobs = cursor.fetchall()

        if not jobs:
            print("No jobs found.")
            return

        print("-" * 40)
        for job in jobs:
            print(f"  ID: {job[0]} | TITLE: {job[1]} | SKILLS: {job[2]}")
        print("-" * 40)

        try:
            job_id = int(input("Enter job ID to delete: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        # Check that the job actually exists before trying to delete
        cursor.execute("SELECT id, title FROM jobs WHERE id = %s", (job_id,))
        job = cursor.fetchone()

        if not job:
            print(f"No job found with ID {job_id}.")
            return

        # Confirm before deleting
        confirm = input(f"Are you sure you want to delete '{job[1]}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Deletion cancelled.")
            return

        cursor.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
        conn.commit()
        print(f"Deleted job '{job[1]}' with ID {job_id}.")

    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()
def update_job():
    print("\nUPDATE JOB")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, title, required_skills FROM jobs")
        jobs = cursor.fetchall()

        if not jobs:
            print("No jobs found.")
            return

        print("-" * 40)
        for job in jobs:
            print(f"  ID: {job[0]} | TITLE: {job[1]} | SKILLS: {job[2]}")
        print("-" * 40)

        try:
            job_id = int(input("Enter job ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        cursor.execute("SELECT id, title, required_skills FROM jobs WHERE id = %s", (job_id,))
        job = cursor.fetchone()

        if not job:
            print(f"No job found with ID {job_id}.")
            return

        print(f"\nUPDATING JOB: {job[1]}")
        new_title = input(f"Enter new title (leave blank to keep '{job[1]}'): ").strip()
        new_skills = input(f"Enter new skills (leave blank to keep '{job[2]}'): ").strip()

        if not new_title and not new_skills:
            return

        updated_title = new_title if new_title else job[1]
        updated_skills = new_skills if new_skills else job[2]

        cursor.execute(
            "UPDATE jobs SET title = %s, required_skills = %s WHERE id = %s",
            (updated_title, updated_skills, job_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Something went wrong: {e}")
    finally:
        cursor.close()
        conn.close()
