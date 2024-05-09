def testers_in_company(test_design_writers,
                       test_scripters,
                       reviewers,
                       out_of_office_today):

    all_testers = list(set(test_design_writers + test_scripters + reviewers + out_of_office_today))

    only_script_testers = []
    testers_at_work_today = []
    write_and_review_testers_today = []

    for i in all_testers:
        if (i not in test_design_writers
                and i not in reviewers
                and i not in only_script_testers):
            only_script_testers.append(i)

        if i not in out_of_office_today:
            testers_at_work_today.append(i)

        if (i in test_scripters
                and i in reviewers
                and i not in out_of_office_today):
            write_and_review_testers_today.append(i)

    return (f"all testers in the team:\n{all_testers},"
            f"\ntesters who can only write scripts:\n{only_script_testers},"
            f"\ntesters who are at work today:\n{testers_at_work_today},"
            f"\ntesters who could write and review scripts, and are at work today:\n{write_and_review_testers_today}")



# print(testers_in_company([1, 3, 5],[2, 3, 4, 6, 7, 8],[1, 2, 3, 9, 10], [2, 5, 6, 1]))


assert testers_in_company([1, 3, 5],[2, 3, 4, 6, 7, 8],[1, 2, 3, 9, 10], [2, 5, 6, 1]) == ("all testers in the team:\n[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
                                                                                           ",\ntesters who can only write scripts:\n[4, 6, 7, 8],"
                                                                                           "\ntesters who are at work today:\n[3, 4, 7, 8, 9, 10],"
                                                                                           "\ntesters who could write and review scripts, and are at work today:\n[3]")
print("Passed")