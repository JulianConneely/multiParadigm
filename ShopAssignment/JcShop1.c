#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Product entity
struct Product
{
  char* name;
  double price;
};
//Stock entity
struct ProductStock
{
  struct Product product;
  int quantity;
};
//Shop entity
struct Shop
{
double cash;
  struct ProductStock stock[20];
};
//Customer entity
struct Customer
{
  char* name;
  double budget;
  struct ProductStock shoppingList[10];
};

void printProduct(struct Product p)
{
  printf("-------------------\n");
  printf("PRODUCT NAME: %s \nPRODUCT PRICE: %.2f\n", p.name, p.price);
  printf("-------------------\n");
}

void printCustomer(struct Customer c)
{
   printf("-------------------\n");
  printf("CUSTOMER NAME: %s \nCUSTOMER BUDGET: %.2f\n", c.name, c.budget);
  printf("-------------------\n");
}

int main(void)
{
  struct Customer julian = {"Julian", 500.0};
  printCustomer(julian);

  struct Product ipa = {"Bottle IPA", 1.10};
  printProduct(ipa);

  struct ProductStock ipaStock = {ipa, 50 };
  // printf("The shop has %d of the product %s\n", cokeStock.quantity, cokeStock.product.name);
  // return 0;
};
