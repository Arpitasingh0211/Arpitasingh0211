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
//insert data at first
struct Node * insertAtFirst(struct Node *head, int data){
  struct Node * ptr = (struct Node *)malloc(sizeof(struct Node));
  ptr -> next = head;
  ptr -> data = data;
  return ptr;  
}
// insert data at nth index
struct Node * insertAtindex(struct Node *head, int data, int index){
  struct Node * ptr = (struct Node *)malloc(sizeof(struct Node));
  struct Node * p = head;
  int i = 0;
  while(i!= index-1)
  {
   p = p->next;
   i++;
  }  
  ptr->data = data;
  ptr->next = p->next;
  p->next = ptr;
  return head;
}
//insert data at the end
struct Node * insertAtend(struct Node *head, int data){
  struct Node * ptr = (struct Node*)malloc(sizeof(struct Node));
  struct Node * p = head;
  ptr -> data = data;
  while(p -> next != NULL)
  {
    p = p -> next;
  }
  p -> next = ptr;
  ptr -> next = NULL;
  return head;
  

}
//insert data after a node
struct Node * insertAfterNode(struct Node *head, struct Node *preNode, int data){
  struct Node * ptr = (struct Node *)malloc(sizeof(struct Node));
  ptr -> data = data;
  ptr -> next = preNode -> next;
  preNode -> next = ptr;
  return head;
}
int main()
{

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

printf("Before insertion\n");
linkedlistTraversal(head);
//head = insertAtFirst(head,56);
// head = insertAtindex(head,56, 2);
//head = insertAtend(head,56);
head = insertAfterNode(head,second,56);
printf("\nAfter insertion\n");
linkedlistTraversal(head);
return 0 ;
}




