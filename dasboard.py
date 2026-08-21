import pandas as pd
import matplotlib.pyplot as plt

def analyze_football_data(csv_file):
    """
    פונקציה שמנתחת נתוני כדורגל מתוך קובץ CSV:
    מדפיסה סטטיסטיקות ועושה הדמיה של נתונים בסיסיים (כמו שערים, בישולים וכו').
    """
    try:
        data = pd.read_csv(csv_file)
    except Exception as e:
        print(f"שגיאה בטעינת הקובץ: {e}")
        return

    print("סטטיסטיקות בסיסיות:")
    print(data.describe(include='all'))

    # דוגמה: הדמיה של שערים לפי קבוצה (אם יש עמודות 'Team' ו-'Goals')
    if 'Team' in data.columns and 'Goals' in data.columns:
        goals_per_team = data.groupby('Team')['Goals'].sum().sort_values(ascending=False)
        print("\nסה\"כ שערים לפי קבוצה:")
        print(goals_per_team)

        goals_per_team.plot(kind='bar', figsize=(10,5), title='סה״כ שערים לפי קבוצה')
        plt.xlabel('קבוצה')
        plt.ylabel('שערים')
        plt.tight_layout()
        plt.show()

    # דוגמה: ניתוח שחקנים עם הכי הרבה שערים (אם יש עמודות 'Player' ו-'Goals')
    if 'Player' in data.columns and 'Goals' in data.columns:
        top_scorers = data.groupby('Player')['Goals'].sum().sort_values(ascending=False).head(10)
        print("\n10 שחקנים עם הכי הרבה שערים:")
        print(top_scorers)

        top_scorers.plot(kind='bar', title='10 שחקנים עם הכי הרבה שערים')
        plt.xlabel('שחקן')
        plt.ylabel('שערים')
        plt.tight_layout()
        plt.show()

# דוגמה לשימוש:
# analyze_football_data('football_data.csv')