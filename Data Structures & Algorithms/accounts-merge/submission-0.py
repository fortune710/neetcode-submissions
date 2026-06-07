class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unique_emails = set()
        email_to_id = {}
        id_to_email = {}
        email_to_name = {}
        

        for account in accounts:
            for index, email in enumerate(account):
                if index == 0:
                    continue
                
                if email not in unique_emails:
                    name = account[0]
                    email_id = len(unique_emails)

                    unique_emails.add(email)
                    email_to_id[email] = email_id
                    id_to_email[email_id] = email
                    email_to_name[email] = name

        parents = [i for i in range(len(unique_emails))]

        def find(root: int):
            while parents[root] != root:
                parents[root] = parents[parents[root]]
                root = parents[root]

            return root

        def union(u: int, v: int):
            u_root = find(u)
            v_root = find(v)

            if u_root == v_root:
                return False

            parents[u_root] = v_root
            return True

        account_groups = {}

        ## First Connect The Accounts
        for account in accounts:
            base_email = account[1]
            for email in account[2:]:
                u = email_to_id[base_email]
                v = email_to_id[email]
                union(u, v)

        ## Then Group The Accounts
        for email, email_id in email_to_id.items():
            root = find(email_id)
            account_groups.setdefault(root, []).append(email)

        ## Then Merge The Groups
        merged_accounts = []

        for key in account_groups:
            emails = account_groups[key]
            name = email_to_name[emails[0]]

            account_list = [name] + sorted(emails)
            merged_accounts.append(account_list)

        return merged_accounts

        


                