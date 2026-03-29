from database import get_connection

def add_job():
    title = input("Enter job title: ")
    skills = input("Enter required skills (separated by comma): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO jobs (title, required_skills) VALUES (%s, %s)", (title, skills))

    conn.commit()
    conn.close()
    print("Job added successfully!\n") 

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
    pass

def delete_job():
    pass

def update_job():
    print("
  UPDATE JOB  ")

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

    print("
 available jobs:")
    for job in jobs:
        print(f"  ID: {job[0]} | TITLE: {job[1]} | SKILLS: {job[2]}")

    try:
        job_id = int(input("
 enter job ID to update: "))
    except ValueError:
        conn.close()
        return

    cursor.execute("SELECT id, title, skills FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()

    if not job:
        conn.close()
        return

    print(f"
 updating job: {job[1]}")
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
