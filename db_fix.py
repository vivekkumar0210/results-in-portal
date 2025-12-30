import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'results_in.settings')
django.setup()

def fix_database_encoding():
    with connection.cursor() as cursor:
        # 1. Database ka default character set badlein
        cursor.execute("ALTER DATABASE defaultdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        
        # 2. Jobs table ko convert karein (Apni table ka sahi naam check kar lena, mostly 'jobs_job' hota hai)
        cursor.execute("ALTER TABLE jobs_job CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        
        print("Database encoding updated to utf8mb4 successfully!")

if __name__ == "__main__":
    fix_database_encoding()