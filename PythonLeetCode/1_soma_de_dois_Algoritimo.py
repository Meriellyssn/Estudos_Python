from typing import List # 1. Importação necessária para usar o List[int]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    #Retornar lista vazia se não houver solução.
        return[]
    # --- ÁREA DE TESTES (Simulando o sistema do LeetCode) ---

    # 2. Criamos os nossos próprios dados de entrada

nums = [2, 7, 11, 15]
target = 9

# 3. "Ligamos" a classe criando um objeto
solucao = Solution()
# 4. Chamamos a sua função passando os nossos dados e guardamos a resposta
resultado = solucao.twoSum(nums, target)
# 5. Mandamos imprimir a resposta no terminal do PyCharm
print(f'Os índices encontrados foram: {resultado}')