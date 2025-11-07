import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS
    print("ALL TESTS")
    cursor.execute('SELECT project_name, test_date, required_strength, actual_strength, passed  FROM concrete_tests')
    first_row = cursor.fetchall()
    failed_i = []
    test_dict = {}
    test_dict_fail = {}
    for i in range(len(first_row)):
        # a = (first_row[i][3]) ? "PASS" : "FAIL"
        if first_row[i][4]:
            a = "PASS"
        else:
            a = "FAIL"
            failed_i.append(i)
        print(first_row[i][0] + ": " + str(first_row[i][3]) + " PSI - " + a)
        if first_row[i][0] not in test_dict_fail and not first_row[i][4]:
                test_dict_fail[first_row[i][0]] = 1
        elif not first_row[i][4]:            
            test_dict_fail[first_row[i][0]] += 1
        if first_row[i][0] not in test_dict:
            test_dict[first_row[i][0]] = 1

        else:
            test_dict[first_row[i][0]] +=1


    
    # 2. Show ONLY failed tests

    print("\nFAILED TESTS")
    # print(failed_i)
    for j in failed_i:
        print(first_row[j][0] + " on " + first_row[j][1])
        print(" Required: " + str(first_row[j][2]) + " PSI")
        print(" Actual: " + str(first_row[j][3]) + " PSI")
        print("\n") 

    # 3. Count tests by project
    print("TESTS PER PROJECT")
    # print(test_dict)
    # print(test_dict_fail)
    for k in test_dict:
        if k in test_dict_fail:
            print(k + ": " + str(test_dict[k] - test_dict_fail[k])+ "/" + str(test_dict[k]) + " passed")

    
    for l in test_dict:
        if l not in test_dict_fail:
            print(l + ": " + str(test_dict[l])+ "/" + str(test_dict[l]) + " passed")
