class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    def add(self, food_id, quantity=1):
        food_id = str(food_id)
        if food_id not in self.cart:
            self.cart[food_id] = 0
        self.cart[food_id] += quantity
        self.save()

    def remove(self, food_id):
        food_id = str(food_id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()

    def clear(self):
        self.session["cart"] = {}
        self.save()

    def save(self):
        self.session.modified = True

