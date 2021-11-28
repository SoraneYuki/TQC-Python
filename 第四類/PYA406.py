while True:

    height = float(input())

    if height == -9999:

        break

    weight = float(input())

    if weight == -9999:

        break

    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:

        state = "under weight"

    elif 18.5 <= bmi < 25:

        state = "normal"

    elif 25.0 <= bmi < 30:

        state = "over weight"

    else:

        state = "fat"

    print("BMI: {:.2f}".format(bmi))
    print("State: {}".format(state))