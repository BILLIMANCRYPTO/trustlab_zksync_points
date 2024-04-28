import requests


def parse_points_earned(wallet_address):
    url = f"https://mp.trustalabs.ai/trustgo/zksync_simu_point?account={wallet_address}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["success"]:
            points_earned = data["data"]["points_earned"]
            return points_earned
        else:
            print("Ошибка при выполнении запроса для кошелька", wallet_address)
            return None
    except Exception as e:
        print("Ошибка при выполнении запроса для кошелька", wallet_address, ":", str(e))
        return None


def main():
    # Открываем файл с кошельками для чтения
    with open("wallets.txt", "r") as f:
        wallets = f.readlines()

    # Удаление символа новой строки из каждой строки
    wallets = [wallet.strip() for wallet in wallets]

    # Проходимся по каждому кошельку
    for wallet in wallets:
        points_earned = parse_points_earned(wallet)
        if points_earned is not None:
            print(f"{wallet}: {points_earned}")

    print("Процесс завершен.")


if __name__ == "__main__":
    main()
