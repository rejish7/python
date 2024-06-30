class laptop:
      def brand(self,new_brand):
            print("the brand is :",new_brand)


class dell(laptop):
      pass

class mac(laptop):
      pass


obj =dell()
obj.brand("dell")
obj1 = mac()
obj1.brand("mac")


