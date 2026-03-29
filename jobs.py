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
