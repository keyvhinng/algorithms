def backtrack(curr, OTHER_ARGUMENTS...):
    if (BASE_CASE):
        # modify answer
        return

    ans = 0

    for (ITERATE_OVER_INPUT):
        # modifiy the current state
        ans += backtrack(curr, OTHER_ARGUMENTS)
        # undo the modification of the current state

    return ans
