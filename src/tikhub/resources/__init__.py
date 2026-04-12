"""Resource modules - one file per OpenAPI tag.

Phase 0 ships ``health_check`` only. Phases 2-5 add the remaining 50 resources
listed in ``PLAN_V3.md`` Part IV. Each resource file follows the same pattern:

* one ``SyncResource`` subclass plus one ``AsyncResource`` subclass
* method name = last segment of the OpenAPI path, verbatim
* parameter names = OpenAPI parameter names, verbatim
"""
