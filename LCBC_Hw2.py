class Solution:
    def isPalindrome(self, head) -> bool:
        if not head or not head.next:
            return True

        # 1. Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 3. Compare the first half with the reversed second half
        left, right = head, prev
        while right: # The reversed half can be shorter for odd-length lists
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True





class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. Find the middle of the list and split it into two halves
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at the middle, head of the second half is slow.next
        second_half_head = slow.next
        slow.next = None # Split the list

        # 2. Reverse the second half of the list
        prev = None
        curr = second_half_head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # 'prev' is now the new head of the reversed second half
        
        # 3. Merge the first half and the reversed second half
        first_ptr = head
        second_ptr = prev # Head of the reversed list
        
        while second_ptr:
            # Save the next nodes
            temp1 = first_ptr.next
            temp2 = second_ptr.next
            
            # Weave the nodes
            first_ptr.next = second_ptr
            second_ptr.next = temp1
            
            # Move to the next pair of nodes
            first_ptr = temp1
            second_ptr = temp2






class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        first_row_has_zero = False
        first_col_has_zero = False
        
        # 1. Check if the first row and column have any zeroes
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
        
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
                
        # 2. Use the first row/col to mark zeroes for the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 3. Set zeroes for the rest of the matrix based on the markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 4. Set zeroes for the first row and column if necessary
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0