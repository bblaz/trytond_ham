from trytond.pool import Pool

__all__ = ['register']


def register():
    Pool.register(
        module='ham', type_='model')
    Pool.register(
        module='ham', type_='wizard')
    Pool.register(
        module='ham', type_='report')
