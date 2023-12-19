class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        doms_dict = {}

        for cpdom in cpdomains:
            count, domain = cpdom.split()
            doms_list = domain.split(".")

            for i in range(len(doms_list)):
                if ".".join(doms_list[i:]) not in doms_dict:
                    doms_dict[".".join(doms_list[i:])] = int(count)
                else:
                    doms_dict[".".join(doms_list[i:])] += int(count)
            print(doms_dict)

        counted_doms = []
        for key, value in doms_dict.items():
            counted_doms.append(str(value) + " " + key)
        
        return counted_doms