def solution(m: int, s: str) -> int:
    n = len(s)
    
    def can_form_k_patterns(k: int) -> bool:
        if k == 0:
            return True
            
        # 如果完全重写字符串的成本在允许范围内
        if k * 3 <= m:  # 只需要插入k个UCC
            return True
            
        # 尝试找到最佳匹配方式
        min_edits = float('inf')
        
        # 考虑所有可能的起始位置
        for start in range(n + 1):
            edits = 0
            pos = start
            patterns = 0
            used = [False] * n  # 标记已使用的字符
            
            # 尝试匹配k个UCC模式
            for _ in range(k):
                if edits > m:
                    break
                    
                # 尝试匹配一个UCC模式
                current_pos = pos
                pattern_edits = 0
                
                # 匹配U
                if current_pos < n:
                    if s[current_pos] != 'U':
                        pattern_edits += 1
                    used[current_pos] = True
                else:
                    pattern_edits += 1
                current_pos += 1
                
                # 匹配两个C
                for _ in range(2):
                    if current_pos < n:
                        if s[current_pos] != 'C':
                            pattern_edits += 1
                        used[current_pos] = True
                    else:
                        pattern_edits += 1
                    current_pos += 1
                
                edits += pattern_edits
                patterns += 1
                pos = current_pos
            
            # 如果成功匹配了k个模式，还需要加上未使用字符的删除成本
            if patterns == k:
                unused_chars = sum(1 for i in range(n) if not used[i])
                edits += unused_chars
                min_edits = min(min_edits, edits)
        
        return min_edits <= m
    
    # 二分查找最大可能的UCC数量
    left, right = 0, (n + m) // 3 + 1
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_form_k_patterns(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return result

if __name__ == '__main__':
    print(solution(m=3, s="UCUUCCCCC") == 3)
    print(solution(m=6, s="U") == 2)
    print(solution(m=2, s="UCCUUU") == 2)