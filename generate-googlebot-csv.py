import csv

GOOGLEBOT_PREFIXES = (
    'johnsmithus',
    'john.smithus',
    'johnsmith.us',
    'john.smith.us',
)

GOOGLEBOT_MIN_NUMBER = 0
GOOGLEBOT_MAX_NUMBER = 99

def main():
    with open('googlebot-email-address.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['Email'])
        writer.writeheader()

        for prefix in GOOGLEBOT_PREFIXES:
            for i in range(GOOGLEBOT_MIN_NUMBER, GOOGLEBOT_MAX_NUMBER+1):
                writer.writerow({
                    'Email': '{}{}@gmail.com'.format(prefix, i)
                })

if __name__ == "__main__":
    main()