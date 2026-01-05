from pyscript import document

def compute_average(event):
    try:
        score1 = float(document.getElementById("score1").value)
        score2 = float(document.getElementById("score2").value)

        average = (score1 + score2) / 2
        result = "Yes" if average >= 75 else "No"

        document.getElementById("average").innerText = str(round(average, 2))
        document.getElementById("result").innerText = result

    except ValueError:
        document.getElementById("average").innerText = "Invalid input"
        document.getElementById("result").innerText = ""
