def model_to_dict(obj):
  output = {}
  for column in obj.__table__.columns:
      # print(column)
    # if obj._sa_class_manager[column].property.secondary in obj._sa_class_manager[column].property:
      output[column.name]=getattr(obj, column.name)
    # else:
      # output[column.name]=getattr(obj, column.name)
  # print(obj.__mapper__.relationships)
  # print(obj.__mapper__.relationships.items())
  for relationship in obj.__mapper__.relationships:
      # print(relationship)
      # print(relationship.argument)
      # print(relationship)
      relations = []
      # print(relationship)
      # print(relationship.key)
      # print(type(relationship.key))
      # print(getattr(obj, relationship.key))
      related_objs = getattr(obj, relationship.key)
      for related_obj in related_objs:
          relations.append(related_obj.name)
      # key = relationship.key
      # print(obj.key)
      # print(type(relationship))
      # for relation in relationship:
      #     print(relation)
      #     if not isinstance(relation, type(NotImplemented)):
      #       print(isinstance(relation, type(NotImplemented)))
      #       print(relation)
      #       print(type(relation))
      #       print(type(relation).name)
      #       print(relation.name)
      #       relations.append(relation.name)
      # print(relations)
      output[relationship.key]=relations
  return output