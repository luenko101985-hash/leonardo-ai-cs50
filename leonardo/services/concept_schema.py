from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints


CleanString = Annotated[str, StringConstraints(strip_whitespace=True)]
NonEmptyString = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1),
]
StringList = list[NonEmptyString]


class StrictModel(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="ignore",
        validate_default=True,
    )


class ExecutionPlan(StrictModel):
    goal: CleanString = ""
    steps: StringList = Field(default_factory=list)
    specialists: StringList = Field(default_factory=list)
    technologies: StringList = Field(default_factory=list)
    estimated_budget: CleanString = ""
    stage_risks: StringList = Field(default_factory=list)
    readiness_criteria: StringList = Field(default_factory=list)
    expected_output: CleanString | StringList = ""


class TechnicalArchitecture(StrictModel):
    system_schema: CleanString = ""
    module_interaction: CleanString = ""
    process_flow: CleanString = ""
    deployment_logic: CleanString = ""


class ResourcesBudget(StrictModel):
    team: StringList = Field(default_factory=list)
    stack: StringList = Field(default_factory=list)
    materials: StringList = Field(default_factory=list)
    cost_notes: CleanString = ""


class StageValidation(StrictModel):
    tests: StringList = Field(default_factory=list)
    kpi: StringList = Field(default_factory=list)
    success_criteria: StringList = Field(default_factory=list)


class ImplementationGuide(StrictModel):
    execution_plan: ExecutionPlan = Field(default_factory=ExecutionPlan)
    technical_architecture: TechnicalArchitecture = Field(
        default_factory=TechnicalArchitecture
    )
    resources_budget: ResourcesBudget = Field(default_factory=ResourcesBudget)
    validation: StageValidation = Field(default_factory=StageValidation)


class ImplementationGuides(StrictModel):
    prototype: ImplementationGuide = Field(default_factory=ImplementationGuide)
    mvp: ImplementationGuide = Field(default_factory=ImplementationGuide)
    pilot: ImplementationGuide = Field(default_factory=ImplementationGuide)
    production: ImplementationGuide = Field(default_factory=ImplementationGuide)


class ImplementationRoadmap(StrictModel):
    prototype: CleanString = ""
    mvp: CleanString = ""
    pilot: CleanString = ""
    production: CleanString = ""


class ConceptData(StrictModel):
    title: NonEmptyString

    leonardo_concept: NonEmptyString
    leonardo_sketch_description: NonEmptyString

    modern_product_name: NonEmptyString
    modern_category: NonEmptyString
    executive_summary: NonEmptyString

    problem_statement: NonEmptyString
    target_users: StringList
    industries: StringList
    use_cases: StringList

    modern_principle: NonEmptyString
    system_components: StringList
    materials: StringList
    technical_requirements: StringList
    modern_sketch_description: NonEmptyString

    implementation_roadmap: ImplementationRoadmap
    implementation_guides: ImplementationGuides
    deployment_strategy: NonEmptyString

    risks: StringList
    constraints: StringList

    market_demand: NonEmptyString
    startup_cost: NonEmptyString
    roi: NonEmptyString
    investor_summary: NonEmptyString

    difficulty: NonEmptyString
    modern_difficulty: NonEmptyString
    dev_time: NonEmptyString


def validate_concept_data(value: object) -> dict[str, object]:
    """Validate and normalize concept data into the UI-facing dictionary contract."""
    return ConceptData.model_validate(value).model_dump(mode="python")
