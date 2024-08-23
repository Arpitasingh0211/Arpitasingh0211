#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
};
void linkedlistTraversal(struct Node * head){
    struct Node *ptr = head;
    do{
        printf("Element: %d\n",ptr -> data);
        ptr = ptr->next;
    }while(ptr != head);
}
//insertion at first
struct Node * insertAtFirst(struct Node *head, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr -> data = data;

    struct Node *p = head ->next;
    while(p -> next != head){
        p = p ->next;
    }
p -> next = ptr;
ptr -> next = head;
head = ptr;
return head;
}

int main(){
struct Node *head;
struct Node * second;
struct Node * third;
struct Node * fourth;

head = (struct Node *)malloc(sizeof(struct Node));
second = (struct Node *)malloc(sizeof(struct Node));
third = (struct Node *)malloc(sizeof(struct Node));
fourth = (struct Node *)malloc(sizeof(struct Node));

head -> data = 11;
head -> next = second;

second -> data = 22;
second -> next = third;

third -> data = 33;
third -> next = fourth;

fourth -> data = 44;
fourth -> next = head;
printf("Before Insertion\n");
linkedlistTraversal(head);
head = insertAtFirst(head,88);
printf("After Insertion:\n");
linkedlistTraversal(head);

return 0;
}
