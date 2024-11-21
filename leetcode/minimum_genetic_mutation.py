from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def generate_mutations(gene: str) -> List[str]:
            mutations = []
            for i in range(len(gene)):
                for nucleotide in 'ACGT':
                    mutations.append(gene[:i] + nucleotide + gene[i+1:])
            return mutations

        bank = set(bank)
        if endGene not in bank:
            return -1
        
        queue = deque([(startGene, 0)])
        while queue:
            current_gene, steps = queue.popleft()
            if current_gene == endGene:
                return steps
            
            possible_mutations = generate_mutations(current_gene)
            for mutation in possible_mutations:
                if mutation in bank:
                    queue.append((mutation, steps + 1))
                    bank.remove(mutation)
        return -1
