from pyscript import document

def compute_average(event):
    # Get the input values and convert to float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)
    score3 = float(document.getElementById("score3").value)
    # Compute average
    average = (score1 + score2 + score3) / 3

    # Determine pass/fail
    if average >= 85:
        result = "Passed"
    else:
        result = "Failed"

    # Display results
    document.getElementById("average").innerText = str(round(average, 3))
    document.getElementById("result").innerText = result
