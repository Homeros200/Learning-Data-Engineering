years = [2026,2027]
months = ["Jan", "Feb"]
days = range(1,29)

for y in years :
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")