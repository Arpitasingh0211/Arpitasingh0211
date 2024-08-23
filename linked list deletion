#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node * next;
};

void linkedlistTraversal(struct Node *ptr)
{
  while(ptr != NULL)
  {
    printf("Element: %d\n", ptr ->data);
    ptr = ptr -> next;
  }

}
//deleting the First Node
struct Node * delFirstNode(struct Node *head){
    struct Node *ptr = head;
    head = head -> next;
    free(ptr);
    return head;
}                        
//deteting a Node in between
struct Node *delAtindex(struct Node *head, int index){
    struct Node *p = head;
    struct Node *q = head ->next;
    for(int i = 0; i < index-1; i++){
      p = p -> next;
      q = q -> next;
    }
    p -> next = q -> next;
    free(q);
    return head;      
}
//deleting the Node at the end
struct Node *delAtEnd(struct Node *head){
    struct Node *ptr = head;
    struct Node *q = head -> next;
   
    while(q -> next != NULL){
      ptr = ptr -> next;
      q = q -> next;
    }
ptr -> next = NULL;
free(q);
return head;
}
//deleting the node by the given index
struct Node *delAtindex2(struct Node *head, int value){
    struct Node *ptr = head;
    struct Node *q = head -> next;
    while(q -> data != value && q -> next != NULL)
    {
        ptr = ptr -> next;
        q = q -> next;
    }
    if(q -> data == value){
        ptr -> next = q -> next;
        free(q);
    }
    return head;
}
int main(){


struct Node * head;
struct Node * second;
struct Node * third;
struct Node * fourth;
//struct Node * head;

head = (struct Node*)malloc(sizeof(struct Node*));
second = (struct Node*)malloc(sizeof(struct Node*));
third = (struct Node*)malloc(sizeof(struct Node*));
fourth = (struct Node*)malloc(sizeof(struct Node*));


head -> data = 7;
head -> next = second;

second -> data = 66;
second -> next = third;

third -> data = 11;
third -> next = fourth;

fourth -> data = 44;
fourth -> next = NULL;

printf("linked list before delation\n");
linkedlistTraversal(head);
// head = delFirstNode(head);
//head = delAtindex(head,2);
//head = delAtEnd(head);
head = delAtindex2(head,11);
printf("linked list after deletion\n");
linkedlistTraversal(head);

return 0;
}




