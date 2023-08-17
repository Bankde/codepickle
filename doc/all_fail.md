FAILED tests/cloudpickle_test.py::CloudPickleTest::test_NamedTuple - OSError: could not get source code
    L1.a.1
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_abc - NameError: name 'abc' is not defined
    L3
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_abstracts - NameError: name 'abc' is not defined
    L3
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_bound_classmethod - AttributeError: 'classmethod' object has no attribute '__globals__'
    L3 - bounded method, maybe also L2
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_classmethod - AttributeError: 'staticmethod' object has no attribute '__globals__'
    L3.a
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_cycle_in_classdict_globals - OSError: could not get source code
    L1.a.2 * (interestingly both cloudpickle and codepickle meddle with the existing class, mark this as *)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_dataclass - OSError: could not get source code
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_deterministic_pickle_bytes_for_function - RuntimeError: Subprocess returned 1: Traceback (most recent call last):
    L1.a.2 (cloudpickle test framework - dumps the loads object: pickle_echo)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_dynamic_module - OSError: could not get source code
    L1.a.2 (Also testframework - subprocess_pickle_echo)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_dynamic_module_with_unpicklable_builtin - OSError: could not get source code
    L1.a.2
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_dynamically_generated_class_that_uses_super - RuntimeError: super(): __class__ cell not found
    L2
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_empty_cell_preserved - Failed: DID NOT RAISE <class 'NameError'>
    L2
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_extended_arg - OSError: could not get source code
    L1.a.2 (cloudpickle test framework - using exec to setup the test)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_final_or_classvar_misdetection - AttributeError: 'property' object has no attribute '__dict__'
    L3.a
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_function_module_name - KeyError: '<lambda>'
    L4 (lambda)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_instance_with_slots - OSError: could not get source code
    L1.a.2 * (not tested but likely same as earlier)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_interactive_dynamic_type_and_remote_instances - RuntimeError: script errored with output:
    L1.a.2 (In _Worker.run, executed run (dumps) on a class several times in a single worker)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_interactive_dynamic_type_and_stored_remote_instances - RuntimeError: script errored with output:
    L1.b (other code in lambda line - w.run)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_interactive_remote_function_calls_no_memory_leak - RuntimeError: script errored with output:
    L2 (side effect from moving closure to globals)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_interactively_defined_function - RuntimeError: script errored with output:
    L1.b (other code in lambda line - subprocess_pickle_echo, also L1.a.2 test framework - subprocess_pickle_echo)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_interactively_defined_global_variable - RuntimeError: script errored with output:
    L1.a.2 (cloudpickle test framework - dumps the loads object: subprocess_pickle_echo)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_lambda -   File "<string>", line 1
    L1.b, L4 (lambda)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_literal_misdetection - AttributeError: 'property' object has no attribute '__dict__'
    L3
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_locally_defined_class_with_type_hints - NameError: name 'type_' is not defined
    L3.b
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_locally_defined_enum - OSError: could not get source code
    L1.a.2 *
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_locally_defined_function_and_class - KeyError: '<lambda>'
    L1.b (lambda) (Also L1.a.2, test framework - subprocess_pickle_echo)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_module_importability - OSError: could not get source code
    L1.a.2 (dynamic module with exec code)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_namedtuple - OSError: could not get source code
    L1.a.1 (namedtuple)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_nested_lambdas - KeyError: '<lambda>'
    L4 (lambda)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_pickle_constructs_from_installed_packages_registered_for_pickling_by_value - NameError: name 'w' is not defined
    L1.b, L4 (lambda)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_pickle_constructs_from_module_registered_for_pickling_by_value - NameError: name '_mock_interactive_session_cwd' is not defined
    L1.b, L4 (lambda, the NamedError is because it's a another function argument, not the lambda)
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_property - AttributeError: 'property' object has no attribute '__dict__'
    L3
FAILED tests/cloudpickle_test.py::CloudPickleTest::test_tornado_coroutine - NameError: name 'gen' is not defined
    L3