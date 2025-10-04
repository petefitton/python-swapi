def model_to_dict(obj):
  output = {}

  for column in obj.__table__.columns:
      output[column.name]=getattr(obj, column.name)

  for relationship in obj.__mapper__.relationships:
      relations = []
      related_objs = getattr(obj, relationship.key)
      for related_obj in related_objs:
          relations.append(related_obj.name)
      output[relationship.key]=relations

  return output