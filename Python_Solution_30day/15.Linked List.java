public static  Node insert(Node head,int data) {
        Node n = new Node(data);
        Node temp = head;
        if (head == null) {
            head = n;
            return head;
        }
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = n;
        return head;
    }